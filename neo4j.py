import json
import requests

class Neo4jDB:
	"""
	This class provides most of the wrapper to the Neo4j REST interface.

	This class defines a connection to a Neo4j 2.0 (milestone 6) 
	REST server and the properties and methods needed to facilitate 
	communication with the database.
	"""

	def __init__(self, url=False):
		# By default, the Neo4j Server URL is set as localhost.
		if url:
			self.__url = url
		else:
			self.__url = 'http://localhost:7474/db/data/'
		# The URL for cypher queries is url + cypher.
		# ie. http://localhost:7474/db/data/cypher
		self.__cypher = self.__url + 'cypher'
		self.__batch = self.__url + 'batch'
		self.__nodes = self.__url + 'node'
		self.__rels = self.__url + 'relationship'

	# URL property
	@property 
	def url(self):
		return self.__url

	# Cypher URL property
	@property
	def cypher(self):
		return self.__cypher

	# Batch URL property
	@property 
	def batch(self):
		return self.__batch

	# Node URL property
	@property 
	def nodes(self):
		return self.__nodes

	# Relationship URL property
	@property 
	def rels(self):
		return self.__rels

	# Headers Property

	def getNode(self, node_id):
		"""Returns the json of the node with the specified node_id."""
		url = self.nodes + '/%r' % node_id
		headers = { "Content-Type": "application/json",
					"Accept": "application/json" }
		r = requests.get( url, headers=headers )
		return r.json()
