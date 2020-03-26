from tax import Taxonomy

tax = Taxonomy()


def test_taxonomy_can_be_created():
    assert tax is not None


def test_nodes():
    human = tax.nodes["9606"]
    assert human == {"id": "9606", "parent": "9605", "rank": "species"}


def test_names():
    cat = tax.names["Felis catus"]
    assert cat == [{"id": "9685", "name": "Felis catus", "type": "scientific name"}]


def test_parental_lineage():
    dog = tax.names["Canus lupus familiaris"]

    lineage = tax.parental_lineage(dog["id"])

    assert [n for n in lineage if n["rank"] != "no rank"] == [
        {"id": "9615", "parent": "9612", "rank": "subspecies"},
        {"id": "9612", "parent": "9611", "rank": "species"},
        {"id": "9611", "parent": "9608", "rank": "genus"},
        {"id": "9608", "parent": "379584", "rank": "family"},
        {"id": "379584", "parent": "33554", "rank": "suborder"},
        {"id": "33554", "parent": "314145", "rank": "order"},
        {"id": "314145", "parent": "1437010", "rank": "superorder"},
        {"id": "40674", "parent": "32524", "rank": "class"},
        {"id": "8287", "parent": "117571", "rank": "superclass"},
        {"id": "89593", "parent": "7711", "rank": "subphylum"},
        {"id": "7711", "parent": "33511", "rank": "phylum"},
        {"id": "33208", "parent": "33154", "rank": "kingdom"},
        {"id": "2759", "parent": "131567", "rank": "superkingdom"},
    ]
