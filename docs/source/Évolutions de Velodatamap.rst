Évolutions de Velodatamap
=========================

Septembre 2024 
--------------

**Signalement :**

* Le mail est désormais renseigné automatiquement à l'ajout d'un signalement si l'utilisateur est connecté
* Pour les catégories « Chaussée » et « Travaux », les maîtres d'ouvrage peuvent maintenant définir une date de début et de fin de validité d'un signalement. Le signalement sera automatiquement archivé le lendemain de sa date de fin de validité
* Seules les véloroutes traversant le territoire de restriction de l'utilisateur connecté sont désormais affichées (simplification visuelle, gain de performances)
* Les champs ``suivistatut`` et ``enquete`` ne sont plus affichés dans le formulaire d'insertion pour les utilisateurs connectés
* Les champs ``remarque_mo`` et ``docuement_complementaire``  ne sont plus affichés dans le formulaire d'insertion pour les utilisateurs non connectés

Août 2024
---------

**Équipement :**

* Une couche ``Véloroutes (isodistance 3km)`` est ajoutée, qui représente les zones situées à moins de 3 km à pied de chaque véloroute. Cela permet de visualiser la recommandation de la fiche-action n°8 de Vélo & Territoires, qui précise qu'une halte-repos ou une aire de services ne doit pas être à plus de 3 km à vélo d'une véloroute
* Seules les véloroutes traversant le territoire de restriction de l'utilisateur connecté sont désormais affichées (simplification visuelle, gain de performances)
* La liste des équipements manquant à un regroupement pour accéder au niveau « Aire de services » est affichée dans sa fiche descriptive
* Il est désormais impossible de créer un équipement ou un regroupement à plus de 3 km d'une véloroute "activée", c'est-à-dire qui s'affiche dans la couche ``Véloroute avec équipement``

Juillet 2024
------------

**Général :**

* Amélioration des performances de l'application
* Implémentation de la charte graphique de l'association (logos, couleurs)
* Pour les utilisateurs ayant une restriction géographique : attribution d'un zoom automatique sur le territoire ou l'itinéraire concerné par la restriction
* Conservation de l'emprise géographique lors du changement de carte
* Changement de plusieurs icônes et attribution de couleurs aux boutons les plus utiles (connexion, ajout d'entité...)


**Équipement :**

* Refonte totale de la structure de la base de données
* Refonte graphique

    * affichage des périmètres des regroupements et itinéraires
    * icônes adaptées au type d'équipement
    * différenciation visuelle des regroupements selon leur statut et importance
    * différenciation visuelle des équipements selon s'ils sont associés à un regroupement ou non
    * légende lisible et exhaustive

* Reprise à zéro des formulaires (infobulles, champs interactifs, tableaux des données liées, méthode des équipements et regroupements…)
* Automatisation

    * les associations équipement et regroupement se font automatiquement à la création des entités
    * champ ``producteur`` renseigné automatiquement selon le nom de l'organisation associée au compte de l'utilisateur
    * l'importance d'un regroupement est déterminée selon les équipements qui lui sont associés

* Nouveaux champs

    * Login du compte ayant créé/modifié la donnée
    * Date de création/modification
    * Distance entre un équipement et son regroupement associé
    * Distance entre un regroupement et les itinéraires auxquels il est associé

* D'avantage de couches disponibles

    * autres véloroutes (sur lesquelles il n'y a pas de dynamique de numérisation d'équipements)
    * limites administratives IGN
    * Plan IGN
    * Photographie aérienne IGN

* Possibilité de filtrer les couches équipement et regroupement selon les valeurs des champs
* Recherche des équipements et regroupements par leur identifiant ou leur nom
* Données équipements et regroupements disponibles à l'export via le requêteur (licence ODbL)
* Mise en place d'un système de restriction géographique (empêche de modifier des données en-dehors de sa collectivité ou de son itinéraire)
* Mise à jour du dictionnaire de données du référentiel national (gabarits, correspondance avec OpenStreetMap…)
* Protection des données personnelles : les logins des créateurs et modificateurs des données n'apparaissent que pour les utilisateurs connectés et sont exclus des exports de données
* Impossibilité d'associer un regroupement à un itinéraire trop lointain
* Optimisation des performances des couches affichées
