# Variables
REGISTRY=rg.fr-par.scw.cloud/namespace-gallant-brown
IMAGE_NAME=pokerbot
TAG=0.0.2

# Full image name
FULL_IMAGE_NAME=$(REGISTRY)/$(IMAGE_NAME):$(TAG)

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

