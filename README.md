{\rtf1\ansi\ansicpg1252\cocoartf2509
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
 **Utilisation de l\'92application OpenFoodFacts**\
\
\
\
\
Arriv\'e9 sur la page principale deux choix s\'92offre \'e0 vous, soit vous souhaitez acc\'e9der \'e0 la base de donn\'e9es openfoodfacts, soit vous acc\'e9dez \'e0 l\'92historique de vos aliments substitu\'e9s.\
\
  \
\
Si vous cliquez sur le bouton \'93Trouver un aliment \'e0 remplacer\'94, vous acc\'e9derez \'e0 une une nouvelle page.\
\
Sur cette page vous devrez tout d\'92abord choisir dans la liste d\'e9roulante, la cat\'e9gorie de l\'92aliment que vous cherchez, vous validez votre choix puis vous choisissez l\'92aliment auquel vous souhaitez acc\'e9der.\
\
Une fois votre choix d\'92aliment valid\'e9, s\'92affichera alors les ingr\'e9dients, le nutriscore, le magasin ou vous pouvez l\'92acheter et le lien de l\'92aliment dans la base de donn\'e9es d\'92openfoodfacts.\
\
  \
\
Sur cette m\'eame page, vous pouvez substituer l\'92aliment que vous avez s\'e9lectionn\'e9, gr\'e2ce \'e0 la liste d\'e9roulante qui affiche les aliments qui appartiennent \'e0 la cat\'e9gorie de l\'92aliment que vous avez pr\'e9c\'e9demment s\'e9lectionn\'e9.\
\
  \
\
Vous pouvez enfin substituer l\'92aliments en cliquant simplement sur le bouton \'93Substituer aliment\'94.\
\
  \
\
Pour acc\'e9der \'e0 l\'92historique des aliments que vous avez substitu\'e9 cliquez, sur cette m\'eame page, sur le bouton \'93Historique\'94.\
\
Vous pouvez aussi acc\'e9dez directement \'e0 cette page, quand vous d\'e9marrez l\'92application sur le bouton \'93Retrouver mes aliments substitu\'e9s\'94.\
\
  \
\
Une fois sur cette page, choisissez tout simplement l\'92aliment qui vous sert de substitut, puis valider.\
\
  \
\
Une fois valid\'e9, sur votre page s\'92affichera sur votre gauche l\'92aliments qui vous sert de substitut avec ses ingr\'e9dients, le nutriscore, le magasin ou l\'92on peut l\'92acheter et le lien, sur votre droite s\'92affiche l\'92aliment qui a \'e9t\'e9 substitu\'e9 ainsi que ses informations.\
\
  \
\
  \
\
  \
\
  \
\
  \
\
  \
\
  \
\
  \
\
  \
\
  \
\
  \
\
  \
\
  \
\
  \
\
La startup Pur Beurre travaille connait bien les habitudes alimentaires fran\'e7aises. Leur restaurant, Ratatouille, remporte un succ\'e8s croissant et attire toujours plus de visiteurs sur la butte de Montmartre.\
\
L'\'e9quipe a remarqu\'e9 que leurs utilisateurs voulaient bien changer leur alimentation mais ne savaient pas bien par quoi commencer. Remplacer le Nutella par une p\'e2te aux noisettes, oui, mais laquelle ? Et dans quel magasin l'acheter ? Leur id\'e9e est donc de cr\'e9er un programme qui interagirait avec la base Open Food Facts pour en r\'e9cup\'e9rer les aliments, les comparer et proposer \'e0 l'utilisateur un substitut plus sain \'e0 l'aliment qui lui fait envie.\
\
Cahier des charges\
\
**Description du parcours utilisateur**\
\
L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :\
\
1 - Quel aliment souhaitez-vous remplacer ?\
\
2 - Retrouver mes aliments substitu\'e9s.\
\
L'utilisateur s\'e9lectionne 1. Le programme pose les questions suivantes \'e0 l'utilisateur et ce dernier s\'e9lectionne les r\'e9ponses :\
\
-   S\'e9lectionnez la cat\'e9gorie. [Plusieurs propositions associ\'e9es \'e0 un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entr\'e9e]\
-   S\'e9lectionnez l'aliment. [Plusieurs propositions associ\'e9es \'e0 un chiffre. L'utilisateur entre le chiffre correspondant \'e0 l'aliment choisi et appuie sur entr\'e9e]\
-   Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas \'e9ch\'e9ant) et un lien vers la page d'Open Food Facts concernant cet aliment.\
-   L'utilisateur a alors la possibilit\'e9 d'enregistrer le r\'e9sultat dans la base de donn\'e9es.\
\
**Fonctionnalit\'e9s**\
\
-   Recherche d'aliments dans la base Open Food Facts.\
-   L'utilisateur interagit avec le programme dans le terminal, mais si vous souhaitez d\'e9velopper une interface graphique vous pouvez,\
-   Si l'utilisateur entre un caract\'e8re qui n'est pas un chiffre, le programme doit lui r\'e9p\'e9ter la question,\
-   La recherche doit s'effectuer sur une base MySql.\
\
Etapes\
\
**1 - Organiser son travail**\
\
D\'e9coupez votre programme en user stories puis en t\'e2ches et sous-t\'e2ches. Cr\'e9ez un tableau agile et affectez des deadlines.\
\
Avant de coder, initialisez un repo Github et faites votre premier push.\
\
Puis commencez \'e0 \'e9crire la documentation. Oui, en premier ! Je vous propose une m\'e9thodologie de travail assez reconnue dans le monde du d\'e9veloppement : le "Doc Driven Development" ou "Readme Driven Development". Cr\'e9ez simplement un fichier texte appel\'e9 Readme.txt.\
\
Vous pouvez utiliser la syntaxe [**Markdown**](https://guides.github.com/features/mastering-markdown/) si elle vous est d\'e9j\'e0 famili\'e8re. Pour cela, appelez simplement votre document Readme.md.\
\
Lorsque vous commencerez une nouvelle fonctionnalit\'e9, \'e9crivez en premier la documentation. Que souhaitez-vous que votre programme fasse ? Comment le d\'e9veloppeur comprendra le code ? Puis codez le n\'e9cessaire pour que votre programme "valide" le Readme.\
\
**2 - Construire la base de donn\'e9es**\
\
Avant de vous atteler aux diff\'e9rentes fonctionnalit\'e9s de votre Readme, commencez par vous questionner sur les informations dont vous avez besoin et dessinez le sch\'e9ma de la base de donn\'e9es. Quelles informations allez-vous enregistrer ? Quelles donn\'e9es allez-vous manipuler ?\
\
Puis int\'e9ressez-vous aux donn\'e9es externes. La base Open Food Facts a une API (exp\'e9rimentale pour le moment) qui vous permet de r\'e9cup\'e9rer les donn\'e9es voulues au format JSON. Vous pouvez consulter la [documentation de cette API](http://en.wiki.openfoodfacts.org/Project:API).\
\
Cr\'e9ez la base de donn\'e9es : tables et cl\'e9s \'e9trang\'e8res.\
\
Puis \'e9crivez un script Python qui ins\'e8rera les donn\'e9es r\'e9colt\'e9es de l'API dans votre base.\
\
Les utilisateurs de la startup Pur Beurre sont fran\'e7ais et font probablement leurs courses en France. Il n'est pas n\'e9cessaire d'importer l'int\'e9gralit\'e9 de la base, d'autant plus qu'elle est si grande que cela ralentirait consid\'e9rablement votre programme (et ferait fuir vos utilisateurs).\
\
**3 - Construire le programme**\
\
Listez les fonctionnalit\'e9s de votre programme pour vous interroger sur les responsabilit\'e9s de chaque classe. Puis construisez l'architecture voulue.\
\
**4 - Interagir avec la base de donn\'e9es**\
\
Vous avez la base de donn\'e9es et vous avez les classes. Bravo ! \'c0 pr\'e9sent, permettez \'e0 votre utilisateur d'interagir avec la base de donn\'e9es.\
\
Commencez par travailler sur le syst\'e8me de question r\'e9ponse (input, validation des champs). Puis concentrez-vous sur la recherche : quelles requ\'eates SQL ? Dans quelle(s) table(s) ?\
\
Enfin, cherchez comment enregistrer les donn\'e9es g\'e9n\'e9r\'e9es par le programme pour que l'utilisateur les retrouve.\
\
Livrables\
\
-   Mod\'e8le physique de donn\'e9es (ou mod\'e8le relationnel) et utilisant l\'92outil informatique de votre choix (pas de dessin \'e0 main lev\'e9e !).\
-   Script de cr\'e9ation de votre base de donn\'e9es\
-   Code source publi\'e9 sur Github\
-   Tableau Trello, Taiga ou Pivotal Tracker.\
-   Document texte expliquant la d\'e9marche choisie, les difficult\'e9s rencontr\'e9es et les solutions trouv\'e9es et incluant le lien vers votre code source sur Github. D\'e9veloppez notamment le choix de l'algorithme et la m\'e9thodologie de projet choisie. Expliquez \'e9galement les difficult\'e9s rencontr\'e9es et les solutions trouv\'e9es. Le document doit \'eatre en format pdf et ne pas exc\'e9der 2 pages A4. Il peut \'eatre r\'e9dig\'e9 en anglais ou en fran\'e7ais, au choix, mais prenez bien en consid\'e9ration que les fautes d\'92orthographe et de grammaire seront \'e9valu\'e9es !\
\
Contraintes\
\
-   Votre code sera \'e9crit en anglais : variables, noms de fonctions, commentaires, documentation, ...\
-   Votre projet sera versionn\'e9 et publi\'e9 sur Github pour que votre mentor puisse laisser des commentaires.}