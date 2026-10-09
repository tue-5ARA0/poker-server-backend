# Variables
REGISTRY=rg.nl-ams.scw.cloud/namespace-pedantic-colden
IMAGE_NAME=pokerbot
TAG=0.1.5

# Full image name
FULL_IMAGE_NAME=$(REGISTRY)/$(IMAGE_NAME):$(TAG)

.DEFAULT_GOAL := build
.PHONY: build push build-and-push print-image-name bump

# Usage: make bump 0.1.5 (the version is a second Make goal).
ifneq ($(filter bump,$(MAKECMDGOALS)),)
ifneq ($(words $(MAKECMDGOALS)),2)
$(error Usage: make bump <version>, for example: make bump 0.1.5)
endif
ifneq ($(firstword $(MAKECMDGOALS)),bump)
$(error Usage: make bump <version>)
endif
export BUMP_VERSION := $(word 2,$(MAKECMDGOALS))
%:
	@:
endif

bump:
	@printf '%s\n' "$$BUMP_VERSION" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+$$' || \
		{ echo 'Usage: make bump <version>, for example: make bump 0.1.5' >&2; exit 1; }
	@sed -i "s/^TAG=.*/TAG=$$BUMP_VERSION/" Makefile
	@sed -i "s|\(image: $(REGISTRY)/$(IMAGE_NAME):\)[^[:space:]]*|\1$$BUMP_VERSION|" deploy/server.yaml
	@echo "Updated Makefile and deploy/server.yaml to $$BUMP_VERSION"

# Build the Docker image
build:
	docker build -t $(FULL_IMAGE_NAME) .

# Push the Docker image to the registry
push:
	docker push $(FULL_IMAGE_NAME)

# Build and push in one command
build-and-push: build push

# Print the full image name (useful for debugging)
print-image-name:
	@echo $(FULL_IMAGE_NAME)
