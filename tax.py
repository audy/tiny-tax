from collections import defaultdict


class Taxonomy:
    def __init__(self, names_path="names.dmp", nodes_path="nodes.dmp"):
        # id -> node
        nodes = {}
        with open(nodes_path) as handle:
            for item in self._parse_nodes(handle):
                assert item["id"] not in nodes, item
                nodes[item["id"]] = item
        self.nodes = nodes

        # name -> [ node, ... ]
        names = defaultdict(lambda: [])
        with open(names_path) as handle:
            for item in self._parse_names(handle):
                names[item["name"]].append(item)
        self.names = dict(names)

    def parental_lineage(self, _id):
        if _id is None:
            return []
        node = self.nodes[_id]
        lineage = [node]
        while True:
            node = self.nodes[node["parent"]]
            lineage.append(node)
            if node["id"] == "1":
                break
        return lineage

    def _parse_names(self, handle):
        for line in handle:
            row = line.strip().split("\t")
            taxid, name, _type = row[0], row[2], row[6]
            yield {"id": taxid, "name": name, "type": _type}

    def _parse_nodes(self, handle):
        for line in handle:
            row = line.strip().split("\t")
            yield {"id": row[0], "parent": row[2], "rank": row[4]}

    def __repr__(self):
        return f"<Taxonomy names={len(self.names)} nodes={len(self.nodes)}>"


if __name__ == "__main__":
    Taxonomy("names.dmp", "nodes.dmp")
