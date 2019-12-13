# Utilisation de l'application OpenFoodFacts


Démmarez le fichier pure_beurre.py

Arrivé sur la page principale deux choix s'offre à vous, soit vous souhaitez accéder à la base de données openfoodfacts, soit vous accédez à l'historique de vos aliments substitués.


Si vous cliquez sur le bouton "Trouver un aliment à remplacer", vous accéderez à une une nouvelle page.

Sur cette page vous devrez tout d'abord choisir dans la liste déroulante, la catégorie de l'aliment que vous recherchez, vous validez votre choix puis vous choisissez l'aliment auquel vous souhaitez accéder.

Une fois votre choix d'aliment validé, s'affichera alors les ingrédients, le nutriscore, le magasin ou vous pouvez l'acheter et le lien de l'aliment dans la base de données d'openfoodfacts.


Sur cette m'eame page, vous pouvez substituer l'aliment que vous avez sélectionné, gr'e2ce à la liste déroulante qui affiche les aliments qui appartiennent à la catégorie de l'aliment que vous avez précédemment sélectionné.


Vous pouvez enfin substituer l'aliments en cliquant simplement sur le bouton '93Substituer aliment'94.


Pour accéder à l'historique des aliments que vous avez substitué cliquez, sur cette m'eame page, sur le bouton '93Historique'94.

Vous pouvez aussi accédez directement à cette page, quand vous démarrez l'application sur le bouton '93Retrouver mes aliments substitués'94.


Une fois sur cette page, choisissez tout simplement l'aliment qui vous sert de substitut, puis valider.


Une fois validé, sur votre page s'affichera sur votre gauche l'aliments qui vous sert de substitut avec ses ingrédients, le nutriscore, le magasin ou l'on peut l'acheter et le lien, sur votre droite s'affiche l'aliment qui a été substitué ainsi que ses informations.













La startup Pur Beurre travaille connait bien les habitudes alimentaires fran'e7aises. Leur restaurant, Ratatouille, remporte un succ'e8s croissant et attire toujours plus de visiteurs sur la butte de Montmartre.

L'équipe a remarqué que leurs utilisateurs voulaient bien changer leur alimentation mais ne savaient pas bien par quoi commencer. Remplacer le Nutella par une p'e2te aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ? Leur idée est donc de créer un programme qui interagirait avec la base Open Food Facts pour en récupérer les aliments, les comparer et proposer à l'utilisateur un substitut plus sain à l'aliment qui lui fait envie.

Cahier des charges

**Description du parcours utilisateur**

L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :

1 - Quel aliment souhaitez-vous remplacer ?

2 - Retrouver mes aliments substitués.

L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :

-   Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
-   Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
-   Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
-   L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.

**Fonctionnalités**

-   Recherche d'aliments dans la base Open Food Facts.
-   L'utilisateur interagit avec le programme dans le terminal, mais si vous souhaitez développer une interface graphique vous pouvez,
-   Si l'utilisateur entre un caract'e8re qui n'est pas un chiffre, le programme doit lui répéter la question,
-   La recherche doit s'effectuer sur une base MySql.

Etapes

**1 - Organiser son travail**

Découpez votre programme en user stories puis en t'e2ches et sous-t'e2ches. Créez un tableau agile et affectez des deadlines.

Avant de coder, initialisez un repo Github et faites votre premier push.

Puis commencez à écrire la documentation. Oui, en premier ! Je vous propose une méthodologie de travail assez reconnue dans le monde du développement : le "Doc Driven Development" ou "Readme Driven Development". Créez simplement un fichier texte appelé Readme.txt.

Vous pouvez utiliser la syntaxe [**Markdown**](https://guides.github.com/features/mastering-markdown/) si elle vous est déjà famili'e8re. Pour cela, appelez simplement votre document Readme.md.

Lorsque vous commencerez une nouvelle fonctionnalité, écrivez en premier la documentation. Que souhaitez-vous que votre programme fasse ? Comment le développeur comprendra le code ? Puis codez le nécessaire pour que votre programme "valide" le Readme.

**2 - Construire la base de données**

Avant de vous atteler aux différentes fonctionnalités de votre Readme, commencez par vous questionner sur les informations dont vous avez besoin et dessinez le schéma de la base de données. Quelles informations allez-vous enregistrer ? Quelles données allez-vous manipuler ?

Puis intéressez-vous aux données externes. La base Open Food Facts a une API (expérimentale pour le moment) qui vous permet de récupérer les données voulues au format JSON. Vous pouvez consulter la [documentation de cette API](http://en.wiki.openfoodfacts.org/Project:API).

Créez la base de données : tables et clés étrang'e8res.

Puis écrivez un script Python qui ins'e8rera les données récoltées de l'API dans votre base.

Les utilisateurs de la startup Pur Beurre sont fran'e7ais et font probablement leurs courses en France. Il n'est pas nécessaire d'importer l'intégralité de la base, d'autant plus qu'elle est si grande que cela ralentirait considérablement votre programme (et ferait fuir vos utilisateurs).

**3 - Construire le programme**

Listez les fonctionnalités de votre programme pour vous interroger sur les responsabilités de chaque classe. Puis construisez l'architecture voulue.

**4 - Interagir avec la base de données**

Vous avez la base de données et vous avez les classes. Bravo ! 'c0 présent, permettez à votre utilisateur d'interagir avec la base de données.

Commencez par travailler sur le syst'e8me de question réponse (input, validation des champs). Puis concentrez-vous sur la recherche : quelles requ'eates SQL ? Dans quelle(s) table(s) ?

Enfin, cherchez comment enregistrer les données générées par le programme pour que l'utilisateur les retrouve.

Livrables

-   Mod'e8le physique de données (ou mod'e8le relationnel) et utilisant l'outil informatique de votre choix (pas de dessin à main levée !).
-   Script de création de votre base de données
-   Code source publié sur Github
-   Tableau Trello, Taiga ou Pivotal Tracker.
-   Document texte expliquant la démarche choisie, les difficultés rencontrées et les solutions trouvées et incluant le lien vers votre code source sur Github. Développez notamment le choix de l'algorithme et la méthodologie de projet choisie. Expliquez également les difficultés rencontrées et les solutions trouvées. Le document doit 'eatre en format pdf et ne pas excéder 2 pages A4. Il peut 'eatre rédigé en anglais ou en fran'e7ais, au choix, mais prenez bien en considération que les fautes d'orthographe et de grammaire seront évaluées !

Contraintes

-   Votre code sera écrit en anglais : variables, noms de fonctions, commentaires, documentation, ...
-   Votre projet sera versionné et publié sur Github pour que votre mentor puisse laisser des commentaires.}