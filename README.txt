								Neo4py
							==============

Neo4py is a Python wrapper to the Neo4j REST interface built on requests and Cypher queries. 


## Quickstart

To set up your connection to the Neo4j Server instance:

	from neo4j import Neo4jDB

	db = Neo4j('YourUrlHere:7474/db/data/')
	# url defaults to localhost:7474/db/data/

	# Get a node by ID:
	db.getNode( node_id ) # returns json response