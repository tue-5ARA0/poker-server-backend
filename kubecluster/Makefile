create-dashboard-token: # create a token to open a dashboard from new machine
	kubectl -n kubernetes-dashboard create token admin-user

forward-dashboard: create-dashboard-token
	echo "http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login"
	kubectl proxy

create-poker-namespace:
	kubectl apply -f poker/namespace.yaml

create-dashboard-user:
	kubectl apply -f dashboard-adminuser.yaml
