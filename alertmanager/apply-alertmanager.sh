#!/bin/bash

TEMPLATE_FILE="alertmanager-templates.yaml"
CRD_FILE="alertmanager-crd.yaml"
CONFIG_FILE="alertmanager-config.yaml"

kubectl apply -f "$TEMPLATE_FILE"
kubectl apply -f "$CRD_FILE"
kubectl apply -f "$CONFIG_FILE"
