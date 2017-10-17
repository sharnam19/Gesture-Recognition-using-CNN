from networks.network import network

if __name__ == "__main__":
    model  = network.load("model.json")
    model.plot()
