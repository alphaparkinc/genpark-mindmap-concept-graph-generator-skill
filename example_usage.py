from client import MindmapGeneratorClient

def main():
    client = MindmapGeneratorClient()
    res = client.generate_mindmap(central_topic='Machine Learning')
    print(f"Result for nodes: {res['nodes']}")

if __name__ == "__main__":
    main()
