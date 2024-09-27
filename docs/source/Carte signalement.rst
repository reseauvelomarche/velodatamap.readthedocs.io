Carte signalement
=================

Cette carte vous permet de visualiser et gérer les signalements d'anomalies cyclable sur les véloroutes qui ont activé l'outil.
L'outil de signalement des anomalies peut être déployé sur toute véloroute présente dans l'Observatoire national des véloroutes. Basé sur la contribution des cyclistes et sur une identification fine des maîtres d'ouvrage et/ou des gestionnaires, l'outil de signalement offre une solution simple et transparente à la gestion d'anomalie. L'usager est assuré que son information est transmise à la bonne personne et cette dernière lui notifie ensuite la résolution du problème rencontré.
Pour plus d'informations sur comment le déployer, son fonctionnement général ou ses connexions avec d'autres outils (FVT, Suricate), vous pouvez vous rendre sur [le site de Vélo & Territoires](https://www.velo-territoires.org/observatoires/outil-signalement-anomalies-cyclables/), cette page étant dédiée à l'utilisation de l'outil sur Velodatamap.

Pour sélectionner, filtrer les données ou afficher la légende, lisez la page des :ref:`Fonctionnalités générales`.

Consulter des signalements
--------------------------

Les signalements sont consultables par toute personne accédant à la carte, connectée ou non. En mode connecté, vous n'aurez accès qu'aux signalements et véloroutes correspondant à vos restrictions géographiques. Cela permet de vous concentrer sur les données qui vous intéressent.

Les signalements créés par des gestionnaires sont en gris, quel que soit leur statut de résolution. Les signalements créés par des usagers sont déclinés en quatre couleurs (rouge, orange, jaune, vert) correspondant aux quatre statuts de résolution (Signalé, Pris en compte, En cours de résolution, Résolu). Cela permet aux gestionnaires de concentrer leur attention sur les signalements d'usagers et pas sur les signalements qu'ils ont eux-même créé.

Créer un signalement
--------------------

Mode public
^^^^^^^^^^^

La carte « Signalement » est accessible à toute personne souhaitant consulter les signalements ou en créer un, sans avoir besoin de se connecter ou d'avoir un compte Velodatamap.

Mode connecté
^^^^^^^^^^^^^

Les seuls utilisateurs ayant accès à la carte « Signalement » en mode connecté sont les gestionnaires et maîtres d'ouvrage identifiés le long des véloroutes ayant déployé l'outil. D'avantage d'options sont disponibles lors de la création d'un signalement, tel que des champs permettant de définir une période de validité pour un signalement (en cas de travaux programmés, ou d'évènement public comme une course automobile), ou un champ permettant de fournir une URL vers un document externe (arrêté municipal, plan de déviation...)
L'adresse mail est automatiquement renseignée à partir du compte Velodatamap. Le statut de résolution est fixé par défaut à « En cours de résolution », ce statut restant modifiable dans le formulaire de création d'un signalement si besoin. 

.. only:: html

    .. figure:: images/gifs/creation_signalement_moe.gif

Modifier un signalement
-----------------------

Seuls les utilisateurs ayant un compte Velodatamap peuvent modifier des signalements. Un utilisateur ne peut modifier que les signalements correspondant à sa restriction géographique, qui devraient être les seuls à apparaître sur son écran de toute façon.
Les gestionnaires peuvent apporter des compléments d'information à la personne ayant créé le signalement en renseignant les champs ``Commentaire du gestionnaire``, ``Document complémentaire`` et ``Photo``. Le statut d'un signalement peut être modifié pour refléter la prise en charge de l'anomalie. Lorsqu'une anomalie est résolue, le statut ``Résolu`` entraînera l'archivage, et donc la disparition de la carte, du signalement après une semaine. Ce délai permet à la personne ayant effectué le signalement de consulter les dernières mises à jour du gestionnaire avant l'archivage du signalement.

Supprimer un signalement
------------------------

La suppression d'un signalement n'est pas autorisée ; seule Vélo & Territoires a le pouvoir de le faire. Si vous avez une bonne raison de vouloir supprimer un signalement au lieu de le passer en statut « Résolu » (doublon, erreur manifeste, etc.), merci de contacter la cellule SIG de Vélo & Territoires.
