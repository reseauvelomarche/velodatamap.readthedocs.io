Fonctionnalités générales
=========================

.. _fonctionnalites:

.. |map_icon| image:: images/map_icon.png

Circuler entre les cartes
------------

Velodatamap a quatre cartes principales : Véloroutes, Équipement, Signalement et Aménagements.
Vous pouvez circuler entre les différentes cartes en cliquant sur l'icône |map_icon| puis en cliquant sur l'une d'entre elles :

.. only:: html

   .. figure:: images/selection_cartes.gif

Activer les différentes couches
------------

Activer la légende
------------

Faire une recherche parmi les données
------------

Filtrer graphiquement les données
------------

Créer, modifier et sélectionner une entité
------------

Comparer des cartes
------------

Mesurer des distances
------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

