provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "capstone" {
  metadata {
    name = "capstone"
  }
}