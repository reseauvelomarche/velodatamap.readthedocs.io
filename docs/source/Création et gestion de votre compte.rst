Création et gestion de votre compte
=====

.. _creation:

Création d'un compte
------------


Si vous êtes une coordination d'itinéraire, nous vous invitons à nous contacter afin d'avoir la liste de tous les comptes activés sur votre itinéraire. À partir de là nous vous transmettrons un formulaire vous permettant de demander de nouvelles créations de compte, ainsi que la modification des droits d'accès de ceux-ci ou encore leur suppression.

Si vous êtes une collectivité individuelle, nous vous invitons à lire la suite de cette documentation pour évaluer si vous auriez un usage d'un compte individuel. Le cas échéant, merci de nous contacter par mail avec les informations suivantes :

- Utilisation prévue de nos outils :
- Nom :
- Prénom :
- Code INSEE de la collectivité territoriale à laquelle vous appartenez :
- Si vous faites partie d'une autre structure (PNR, Syndicat d'initiative, Bureau d'étude...) :
   - l'ensemble des codes INSEE de vos collectivités adhérentes ou pour le compte desquelles vous intervenez :
   - Nom de votre structure :
- Accès au module équipements : oui/non
- Accès au module signalement : oui/non
- Activation des notifications mail pour le signalement : oui/non

Vélo & Territoires créera votre compte dans la semaine qui vient, après quoi vous recevrez un mail automatique avec le résumé de vos différents accès, votre identifiant et un mot de passe provisoire qu'il vous sera obligatoire de changer à votre première connexion.

Gestion et modification d'un compte
----------------

Pour modifier vos accès aux différents modules de Velodatamap, merci de nous contacter.

Pour modifier votre mot de passe, il suffit d'accéder à l'interface de connexion et de suivre la démarche suivante :

.. only:: html

   .. figure:: images/oubli_mot_de_passe.gif


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

