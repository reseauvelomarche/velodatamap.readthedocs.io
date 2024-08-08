Fonctionnalités générales
=========================

.. _fonctionnalites:

.. |map_icon| image:: images/map_icon.png
.. |layer_icon| image:: images/layer_icon.png

.. only:: html

    .. figure:: images/selection_cartes.gif

:::{dropdown} Circuler entre les cartes

Velodatamap a quatre cartes principales : Véloroutes, Équipement, Signalement et Aménagements.
Vous pouvez circuler entre les différentes cartes en cliquant sur l'icône |map_icon| puis en cliquant sur l'une d'entre elles :
:::






Activer les différentes couches de données
------------

Différentes couches de données peuvent être affichées sur chaque carte. Certaines s'affichent par défaut dès le chargement, et d'autres sont désactivées par défaut mais peuvent vous être utiles !
Cliquez sur |layer_icon| pour accéder à l'interface suivante :

.. only:: html

   .. figure:: images/selection_cartes.gif

Afficher la légende
------------

Besoin de comprendre les données qui s'affichent sur la carte ? Affichez la légende propre à chaque carte, toujours en cliquant sur |layer_icon| :

.. only:: html

   .. figure:: images/legende.gif


Faire une recherche parmi les données
------------

Filtrer graphiquement les données
------------

Créer, modifier et sélectionner une entité
------------

Exporter des données
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

