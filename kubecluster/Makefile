create-dashboard-token: # create a token to open a dashboard from new machine
	kubectl -n kubernetes-dashboard create token admin-user

forward-dashboard:
	kubectl port-forward -n kubernetes-dashboard service/kubernetes-dashboard 8443:443

create-poker-namespace:
	kubectl apply -f poker/namespace.yaml

create-dashboard-user:
	kubectl apply -f dashboard-adminuser.yaml