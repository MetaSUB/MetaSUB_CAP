**********************
Database API Reference
**********************

DataSuper provides a Python API 

Setting up and loading a repo
=====================

Setting up a new repo takes just one line of code::

  from datasuper import *

  repoDir = '/foo'
  Repo.initRepo( targetDir=repoDir)

Unless otherwise specified this will create a repo in the current working directory.

The repo object
=====================

.. addFileType(typeName)
   adds a new file type to the available list


.. addResultSchema( self, resultType, resultSchema)
   adds a new result schema to the available list
   
Information Retrieval
=====================


Information Retrieval
=====================
