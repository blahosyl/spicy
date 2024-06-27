<!--Shield.io badges-->

# Spicy Recipes

A recipe blog for autistic and other neurodiverse folx. Utilitarian, customizable and to the point. No rambling, no unrelated stories, no word count fillers, no distracting desgin kitsch or vertigo-inducing moving backgrounds. Instead, the focus is on precise and searchable information to easily find recipes for specific needs.

Developer: [Dr. Sylvia Blaho](https://www.linkedin.com/in/blahosylvia/)


![Deployed site starting screen](readme-pics/amiresponsive/cover-amiresponsive.png)
[Go to the deployed app](https://spicy-recipes-django-5d174ffc7c94.herokuapp.com/)

See the development progress and further plans on [GitHub Projects](https://github.com/users/blahosyl/projects/5/views/2).

![GitHub last commit](https://img.shields.io/github/last-commit/blahosyl/spicy?color=red)
![GitHub contributors](https://img.shields.io/github/contributors/blahosyl/spicy?color=orange)
![GitHub language count](https://img.shields.io/github/languages/count/blahosyl/spicy?color=black)

## Table of Contents

## UX/UI

### Strategy

In a world designed for neurotypical people, the needs of neurodivergent people are often disregarded. When it comes to recipe blogs, the 3 main culprits I aim to tackle in this project are

- [superfluos information](#superfluos-information)
- [lack of specificity](#lack-of-specificity)
- [lack of customization](#dopamine-design)

Each issue and its implemented remedy is described below.

#### Superfluos information

An [oft-parodied trend](https://www.facebook.com/reel/771271748497011) of many food blogs is their inflated word count by paraphrasing and unlerated personal stories, presumably in an effort to improve their SEO ranking.

While this is a mild annoyance to neutotypical people, it can be a serious accessibility issue for those who are neurodivergent and have executive functioning issues, such as problems focusing or [front-end perfectionism](https://www.psychologytoday.com/us/blog/rethinking-adult-adhd/202012/adult-adhd-perfectionism-and-procrastination).

#### Lack of specificity

Many autistic people are very particular about food (termed [food selectivity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10488249/) in scientific literature; [some](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10488249/table/jcm-12-05469-t002/?report=objectonly) [examples](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10488249/table/jcm-12-05469-t004/?report=objectonly)). However, most recipe blogs do not offer easy ways to search for particular textrues, tastes or temperatures.

#### Dopamine design

Analogous to [dopamine dressing](https://fromtheslowlane.com/anywhere/fashion/what-is-dopamine-dressing/), being able to surround themselves with colors that match or complement their mood and energy levels is a useful coping strategy for neurodivergent people.


### Scope

#### Clearly separated fields for creating and viewing recipes

To combat the problem of [superfluos information](#superfluos-information), this recipe site is designed to clearly separate the different components of a recipe to provide a better overview for visitors, and a helpful template for recipe writers.

#### Searching and filtering

To address the problem of [lack of specificity](#lack-of-specificity), this recipe blog has an emphasis on tagging, searching and filtering recipes, enabling visitors to find recipes matching their specific needs.


#### Alternative color themes

To facilitate users being able to [customize the look of the site](#dopamine-design), the blog offers a selection of color themes that users can chose from.

#### Planning and prioritization

Along with usual blog features like access management, post management and collaboration, the following Themes, Epics and User Stories were defined at the beginning of the project:

![Initial scope of project](readme-pics/user-stories/pp4-user-stories-initial.png)

However, as the development time available for the project was only 1 month, and this was my first Django project, these User Stories were vetted based on whether they were to be part of the Minimum Viable Product (MVP) or not.

Based on the considerations specific to a neurodivergent audience (described above), clarity of presentation and customizability was rated more important than collaboration.

Accordingly, the User Stories in the MVP were determined as follows:

![Initial scope of the MVP](readme-pics/user-stories/pp4-user-stories-initial-mvp.png)

Naturally, this list was modified somewhat during development (see the [Prioritization](#prioritization) section for details). The final list can be seen in [GitHub Issues](https://github.com/blahosyl/spicy/issues?page=2&q=is%3Aissue+label%3A%22p%3A+must+have%22+-label%3A%22epic%22+-label%3A%22e%3A+readme%22+-label%3A%22e%3A+testing%22+-label%3A%22e%3A+code+validation%22+-label%3A%22e%3A+code+structure+%26+comments%22+-label%3Abug).

### Structure

#### Data models

The initial design of data models was as follows:

![Initial ERD](readme-pics/erd-initial.png)

Notable aspects of the models are described below.

##### Recipe model

Partially based on the Post model of the I Think Therefore I Blog walkthrough, but changed several aspects:

- Published is Boolean
- Separated content into
	- Instructions
	- PrepTime
	- CookTime
	- Ingredients (separate model)

##### Ingredient & IngredientQuantity models

Ingredients are available across the project, while IngredientQuantities are specific to individual recipes.

The reasoning behind this setup was threefold:

1. To allow for more fine-grained access permissions
2. To lay the foundations for a future implementation of a shopping list making functionality, along the lines of the [Dinner Party app I made](https://github.com/blahosyl/dinner-party/).
3. The intermediary IngredientQuantity model also has unit and quantity attributes. 

###### Quantity data type

[Decimal](https://docs.python.org/3/library/decimal.html#module-decimal) instead of float used for quantity.

###### IngredientQuantity not compulsory

Recipes can be saved without any ingredients (to allow better management of  drafts).

###### Instances of Ingredient cannot be duplicated

Instances of ingredient where `ingr_name` & `preparation` is the same cannot be duplicated. 

- "cheese, sliced" and "cheese, grated" are both possible
- 2 instances of "cheese, grated" are not allowed

This is true when added new ingredients as well as when editing exisitng one would result in a duplicated.

###### IngredientQuantities **can** be duplicated

Each instance of IngredientQuantity is unique, that is, even if there are 2 recipes that call for 2 apples each, these are treated as separate entities.

##### Comment model

This model is based entirely on the Comment model of the [I Think Therefore I Blog walkthrough project]((https://github.com/Code-Institute-Solutions/blog)).

##### RecipeAttribute and Attribute models

These models were added to the intial desgin in order to enable more filtering and more precise tagging of recipes. 
Their implementation parallels IngredientQuantity and Ingredient:
RecipeAttribute acts as an intermediary between the Recipe and Attribute models.

Using this design as oppsed to a ManyToManyField relation between Recipe and Attribute enables setting up a better control of the scope of permissions for staff users.

##### Profile model

When implementing the `community` app of the project, this model was added to store public information about the users, with the intention that logged-in users will be able to create and manage profiles for themselves.

Crucially, the Profile model is distinct from the built-in User model, connected by a OnetoOne field. 

There are 2 advantages to this setup:

1. Allow for user information to be accessible in the admin panel but not on the website UI
2. Avoid accidentally overwriting crucial user information needed for signin and permissions.

Accordingly, the current Entity Relationship Diagram is as follows:

![Initial ERD](readme-pics/erd-final.png)

#### UI information design

##### Navigation bar

This is present on every page, thus it contains elements that are used throughout the site.

The most prominent position has the navigation links letting the user switch between the `collection` app containing the reicpes, and the `community` app containing the user profiles.

The center position of the nav bar has the blog name, logo and tagline.

On the right, we find the color theme selector toggle and the recipe search bar, but of these being important targeted features of the project.

##### Collection app

As the primary purpose of the project is to show recipes, the home page of the site displays the list of published recipes. 

The recipe filters are prominently placed at the top, since it is anticipated that this feature will be widely used by the target audience.

Clicking on any recipe takes the visitor to the recipe detail page.

##### Community app

To ease navigation, this app is laid out similarly to the `collection` app: the main page show a list of profiles, and clicking on them leads to the profile detail page.

##### Footer

The footer is also present on every page, but the information contained here is predicted to be used less frequently: the developer name and social media profile links.

### Skeleton

#### Home page wireframes

Since this recipe blog is modelled after the [I Think Therefore I Blog walkthrough project](https://github.com/Code-Institute-Solutions/blog), and one of the project's aims is to keep layouts simple and intuitive, the basic layout of the home page and footer was not modified significantly (see the [UX improvements](#ux-improvements) section for changes that might not be obvious at first glance).

However, I decided to make several alterations and additions to the navigation bar.

First, I visually separated page navigation from account management functions (signing up/in/out): the page navigation stayed in the top left corner in the navigation, but account management links and information were moved to the so-called "user bar" immediately below.

Within the user bar, (semi-)permanent information was moved to the right side, while the left portion of the user bar was reserved for ephemeral dismissable messages having to do with signing in/out.

![Wireframe for recipe list | desktop](readme-pics/wireframes/recipe-list-desktop.png)

I also moved the blog name to the middle of the navigation bar.

The right side of the navigation bar has the color theme toggle and the search field.

The mobile version of the recipe list (with the nav bar open) was mocked up as follows:

![Wireframe for recipe list | mobile](readme-pics/wireframes/recipe-list-mobile-nav-open.png)

#### Recipe detail wireframes

I have made some more significant changes to the recipe detail page, since the way the data are stored is also more detailed than in the walkthrough project.

I separated the space under the masthead into 2 columns: the smaller one on the left has concrete, bite-sized and easily parsable information like preparation time, cooking time and ingredients. The larger column on the right contained the instructions.

![Wireframe for recipe detail page | desktop](readme-pics/wireframes/recipe-detail-desktop.png)

Not shown on the wireframes is the **Comments** section – since this is very much the same as the walkthrough project, I did not make a separate mockup of this. One change I implemented was to show messages to do with comment creation/editing/deletion in the comment section rather than at the top of the page (see the section [UX improvements](#ux-improvements)).

A further addition to the masthead on the recipe detail page is the inclusion of attribute tags.

The mockup of the  mobile version of the recipe detail page is shown below (with the nav bar closed):

![Wireframe for recipe detail page | mobile](readme-pics/wireframes/recipe-detail-mobile-nav-closed.png)

I did not make separate wireframes for the profile list and profile detail templates, as these are analogous to their corresponding recipe counterparts.

### Surface

Design

#### UX Improvements

The names of the navigation links were later changed to **Collection** and **Community**, to better reflect the names of the apps.

 On the recipe list and the profile list, the whole card was made clickable instead of just the title, to accommodate those with below average motor coordination (another frequent occurrence within neurodivergent individuals).

 Separated messages


## Project Management | Agile

### Agile Methodologies

#### Themes, Epics, Stories & Tasks

##### Prioritization

The links below show User Stories excluding "meta" issues such as testing & documentation.

- [User Stories with priority `must have`](https://github.com/blahosyl/spicy/issues?page=2&q=is%3Aissue+label%3A%22p%3A+must+have%22+-label%3A%22epic%22+-label%3A%22e%3A+readme%22+-label%3A%22e%3A+testing%22+-label%3A%22e%3A+code+validation%22+-label%3A%22e%3A+code+structure+%26+comments%22+-label%3Abug): 39
- [User Stories with priority `should have`](https://github.com/blahosyl/spicy/issues?q=is%3Aissue+label%3A%22p%3A+should+have%22+-label%3A%22epic%22+-label%3A%22e%3A+readme%22+-label%3A%22e%3A+testing%22+-label%3A%22e%3A+code+validation%22+-label%3A%22e%3A+code+structure+%26+comments%22+-label%3Abug+-label%3Av2+): 11
- [User Stories with priority `could have`](https://github.com/blahosyl/spicy/issues?q=is%3Aissue+label%3A%22p%3A+could+have%22+-label%3A%22epic%22+-label%3A%22e%3A+readme%22+-label%3A%22e%3A+testing%22+-label%3A%22e%3A+code+validation%22+-label%3A%22e%3A+code+structure+%26+comments%22+-label%3Abug+-label%3Av2+): 28

The statistics on planned vs. implemented User Stories can be seen on the **Statistics** tab of the [User Stories Google Sheet](https://docs.google.com/spreadsheets/d/1QDYJlX4RVgoKokpcXgFkGtmrwcCMplf8XZcpNxoEYRU/edit?gid=1814855102#gid=1814855102).


Epics that had User Stories of various levels of prioritization received all applicable labels. As the User Stories in the Epic were completed, the labels of completed User Stories were removed from the Epic.

For example, [EPIC: View author info](https://github.com/blahosyl/spicy/issues/27) has one User Story with priority `should have` completed, and another User Story with priority `could have` remaining to be done, so it now only has the label `p: could have`.

#### Project Board

#### Labels

#### Prioritization & reprioritization

#### Timeboxing

#### Sprint planning

#### Sprint retroactives

## Features

## Technoogies used

### Languages & frameworks used

### Tools used

- [Freeconvert](https://www.freeconvert.com/): convert manual testing videos from `.mov` to `.mp4`

### Deveopment process

## Depoyment

The following instrcutions describe the deployment process with the tools used for this project. 
Of course, you can choose other tools/providers for the individual functions described below, e. g., a different Postgres database instead of Neon, or a different development environment instead of GitPod. 
Naturally, detailed instructions are only provided for the tools used in this project.

### Prerequisites

- [GitPod](https://www.gitpod.io/) (or another IDE)
- [Python 3](https://www.python.org/downloads/release/python-385/)
- [pip](https://github.com/pypa/pip)
- [git](https://git-scm.com/)
- [Neon](https://neon.tech/) (or another Postgres database)
- [Cloudinary](https://cloudinary.com/) (or another media hosting provider)
- [Google Mail](https://google.com) with an [app password](https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237) (or another email server)
- [Heroku](https://www.heroku.com/) (or another could platform)

### Fork the repository

You can fork the repository by following these steps:

1. Log in to [GitHub](https://github.com/) (if you don't have a GitHub account yet, you can [create one](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) for free).
2. Navigate to the project website [https://github.com/blahosyl/spicy](https://github.com/blahosyl/spicy).
3. Click on **Fork** in the upper right part of the screen.
4. On the next page you have the possibility to change the repository name. To do this, simply write your desired name in the text field in the center part of the screen. You can also leave the name as it is.
5. Click **Fork** in the bottom right part of the screen.

>[!TIP]
>If you do rename the repository, make sure to keep the [GitHub naming conventions](https://github.com/bcgov/BC-Policy-Framework-For-GitHub/blob/master/BC-Gov-Org-HowTo/Naming-Repos.md) in mind.

### Deploy in the development environment

1. Open the repository in a new workspace in GitPod. GitPod will automatically run the Python virtual environment for you. If you're using a different development environment, see [this documentation](https://docs.python.org/3/library/venv.html).
2. Install the required dependencies:
	```
	pip3 -r requirements.txt.
	```
3. To store access credentials and other secrets, create a file called `env.py` in your top-level projct directory. 
Before adding any content to it, add `env.py` to `.gitignore` and commit your changes. 
This will prevent the contents of `env.py` from being pushed to the Git repository.
4. Add the following information to your `env.py` file:
  	- `CLOUDINARY_URL` -you can find this in your [Cloudinary](https://cloudinary.com/) console under **API Keys**
	- `DATABASE_URL`
	- `DEFAULT_FROM_EMAIL`
	- `SECRET_KEY`
5. In `settings.py`, add your GitPod workspace URL to `ALLOWED_HOSTS`
6. Run a migration to create your database tables:
	```
	python manage.py migrate
	```
7. Create a superuser (make sure you save the username and password you use here):
	```
	python manage.py createsuperuser
	```
8. Run the development server
	```
	python manage.py runserver
	```

### Deploy to production

#### Pre-deployment steps

Make sure to complete the following pre-deployment steps in your development environment, especially if you made changes to the project:

1. (Re-)create a list of requirements by going to the terminal and typing `pip3 freeze > requirements.txt`. This popuplates your `requirements.txt` file with the list of required files.
2. Collect static files (these are hosted with [whitenoise](http://whitenoise.evans.io/en/stable/)):
	```
	python manage.py collectstatic
	```
3. In `settings.py`, make sure `DEBUG=False`
4. Commit and push your changes to GitHub.

#### Steps on Heroku

1. Log in to your [Heroku](https://www.heroku.com/) account (or create a new one if you have not done so yet).
2. [Create a new Heroku app](https://dashboard.heroku.com/new-app) by selecting your region and app name.
3. Under **Settings > Config Vars** in Heroku, add the following variables:
	- `CLOUDINARY_URL` -you can find this in your [Cloudinary](https://cloudinary.com/) console under **API Keys**
	- `DATABASE_URL`
	- `DEFAULT_FROM_EMAIL`: this can be the same as `EMAIL_APP_USER`
	- `EMAIL_APP_PASSWORD`: [instructions for obtaining one](https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237)
	- `EMAIL_APP_USER`: the email used with your email server
	- `SECRET_KEY`
4. Under **Deploy > Deployment method** in Heroku, select **GitHub** and connect Heroku to your GitHub account.
	- Type in your repository name, then click **Search**. 
	- When your repository appears, click **Connect** next to it.
5. Under **Deploy > Manual deploy** in Heroku, select **Deploy branch** to deploy manually.
	- Once the process is finished, the following message will appear:<br>
	_Your app was successfully deployed_
	- Click **View** under the message, and a new tab will appear with your deployed app.
6. (optional) Under **Deploy > Automatic deploy** in Heroku, select **Enable Automatic Deploys** if you want your app to be rebuilt each time you push to the `main` branch of your GitHub repository (but make sure your `settings.py` file always has `DEBUG=False` when you do). 

## Testing

See the document [`TESTING.md`](TESTING.md) for details.

## Credits

### Code credits

- The architecture of the project was based on the [I Think Therefore I Blog walkthrough project](https://github.com/Code-Institute-Solutions/blog) by Code Institute
- Leon Potgieter suggested I use Neon DB when I discovered ElephantSQL's EOL, helped with [testing on local DB issue](https://code-institute-room.slack.com/archives/C02B3MJQABA/p1716915411743489?thread_ts=1716855535.547499&cid=C02B3MJQABA), and gave me a [handy tip for line breaking](https://code-institute-room.slack.com/archives/C06JCL29EBD/p1718953195099119?thread_ts=1718941634.864539&cid=C06JCL29EBD) 
- [search tutorial](https://learndjango.com/tutorials/django-search-tutorial)
- [querying of related models](https://github.com/blahosyl/spicy/issues/115) implemented with the help of [Roman Rakic](https://code-institute-room.slack.com/archives/C026PTF46F5/p1718633149758449?thread_ts=1718600949.810239&cid=C026PTF46F5)
- [Tech Corner Website](https://github.com/j0hanz/tech-corner-website)
- [Successful comment editing test](https://github.com/blahosyl/spicy/commit/50c3f7d6f3f79a7f296d018503cacb05ae3bfbe2)  rewritten with the help of tutor Roo

### Related advice

- [Daisy McGirr on the Allauth social plugin](https://code-institute-room.slack.com/archives/C026PTF46F5/p1717142987306069?thread_ts=1717110872.353119&cid=C026PTF46F5)
- [Rachel O'Donnell](https://code-institute-room.slack.com/archives/C026PTF46F5/p1719421906829349?thread_ts=1719420790.046999&cid=C026PTF46F5) and [Joanna Gorska](https://code-institute-room.slack.com/archives/C026PTF46F5/p1684951227697019?thread_ts=1684831337.699099&cid=C026PTF46F5) on how to allow creating mockups with [amiresponsive](https://ui.dev/amiresponsive) by installing the [Ignore X-Frame Headers Chrome plugin](https://chromewebstore.google.com/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe)



### Study/lookup sources

The following resources were used to learn/double check general, atomic functionalities/syntax/errors:


- [Show labels and Milestones in GitHub Projects Kanban board](https://github.com/orgs/community/discussions/10788)
- [Creating and editing milestones for issues and pull requests](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/creating-and-editing-milestones-for-issues-and-pull-requests)
- [making a model for ingredients](https://groups.google.com/g/django-users/c/DtkxblwqWbE/m/zJfqURzgxkUJ)
- [sort model entries by field](https://www.geeksforgeeks.org/durationfield-django-models/)
- [connector types in Entity Relationship Diagrams](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning)
- [float vs. decimal in Python](https://docs.python.org/3/library/decimal.html#module-decimal)
- [`durationfield` in Django](https://www.geeksforgeeks.org/durationfield-django-models/)
- [1:N relationship where N must be at least one entry](https://stackoverflow.com/questions/7310121/1n-relationship-where-n-must-be-at-least-one-entry)
- [database design one to many where many is at least one](https://stackoverflow.com/questions/655074/database-design-one-to-many-where-many-is-at-least-one)
- [Django model reference](https://docs.djangoproject.com/en/4.2/ref/models/)
- [`verbose_name`: change model display name in admin panel](https://forum.djangoproject.com/t/django-admin-page-edit-app-names/14720)
- [inline model in admin panel | Django documentation](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.TabularInline)
- [inline model in admin panel | Stackoverflow](https://stackoverflow.com/questions/33748059/add-inline-model-to-django-admin-site)
- [exclude duplicates of the same two fields together](https://stackoverflow.com/a/20243795)
- [pluralize words depending on database value](https://testdriven.io/tips/db65f09a-06a4-4a8f-843f-a83a49b2f0c7/)
- [Bootstrap spacing](https://getbootstrap.com/docs/5.0/utilities/spacing/)
- [Bootstrap position](https://getbootstrap.com/docs/5.0/utilities/position/)
- [Bootstrap cards](https://getbootstrap.com/docs/5.0/components/card/)
- [Bootstrap grid system](https://getbootstrap.com/docs/5.0/layout/grid/)
- [change CSS color variables with JS](https://www.toptal.com/front-end/dynamic-css-with-custom-properties)
- [Bootstrap nav bar](https://getbootstrap.com/docs/5.0/components/navbar/)
- [Keep form elements on one line with Bootstrap](https://stackoverflow.com/a/69603236)
- [Bootstrap forms | select](https://getbootstrap.com/docs/5.0/forms/select/)
- [HTML symbols](https://www.w3schools.com/html/html_symbols.asp)
- [trailing slashes in URIs](https://cdivilly.wordpress.com/2014/03/11/why-trailing-slashes-on-uris-are-important/)
- [Bootstrap: make whole card clickable](https://getbootstrap.com/docs/5.0/helpers/stretched-link/)
- [Allauth documentation](https://docs.allauth.org/)
- [Allauth guide](https://dev.to/gajesh/the-complete-django-allauth-guide-la3)
- [email verification: email must be required](https://stackoverflow.com/a/78066852)
- [email verification in the Dev environment](https://code-institute-room.slack.com/archives/C026PTF46F5/p1706728353289989?thread_ts=1684774840.781519&cid=C026PTF46F5)
- [email verification example](https://github.com/tlalexandre/HugoMarquisCoaching/blob/main/HugoMarquisCoaching/settings.py)
- [managing static files in Django](https://docs.djangoproject.com/en/5.0/howto/static-files/)
- [change app name (used by Allauth emails)](https://stackoverflow.com/a/30017741)
- [Git merge vs rebase](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)
- [recorver deleted GitHub branch](https://github.com/orgs/community/discussions/55884)
- [direct link to Google app passwords](https://support.google.com/mail/thread/267471964?hl=en&msgid=268430543)
- [`Attribute error (missing)` caused by indentation error in `views.py`](https://stackoverflow.com/a/64709139)
- [Mozilla JS `sessionStorage` docs](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage)
- [Mozilla Web Storage API docs](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API)
- [JS local storage intro](https://www.freecodecamp.org/news/use-local-storage-in-modern-applications/)
- [Mozilla JS `querySelector` documentation](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
- [Javascript docstrings](https://jsdoc.app/about-getting-started)
- [many-to-many relationships in Django](https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django)
- [intermediary table vs. ManyToManyField](https://www.reddit.com/r/django/comments/awgt3q/is_it_better_to_use_multiple_foreignkey_in_an/)
- [Django documentation on many-to-many relationships](https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_many/)
- [accessing foreign key valies in ListView](https://stackoverflow.com/questions/52649906/accessing-foreign-key-values-in-django-listview-of-gcbv)
- [querying backwards related objects](https://docs.djangoproject.com/en/4.2/topics/db/queries/#backwards-related-objects)
- ["`ReverseManyToOneDescriptor` object has no attribute" error](https://stackoverflow.com/questions/40250430/reversemanytoonedescriptor-object-has-no-attribute-latest)
- [Django search documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/search/)
- [display search term on search result page](https://stackoverflow.com/a/70825490)
- [how to reuse the same bit of code in Django](https://stackoverflow.com/a/43457105)
- [Django `include` documentation](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#include)
- [relative paths for templates](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#std-templatetag-extends)
- [fix pagination for search results](https://stackoverflow.com/q/64353780)
- [dropdown form in Django](https://stackoverflow.com/a/54584865)
- [dropdown form without a button](https://stackoverflow.com/a/59007468)
- [conditional: string in URL](https://stackoverflow.com/a/12877568)
- [`elif` vs `else` error: "Exception Value: Unexpected end of expression in if tag"](https://stackoverflow.com/questions/65132837/django-exception-value-unexpected-end-of-expression-in-if-tag)
- [set Cloudinary to use https](https://stackoverflow.com/a/62096398)
- [`import cloudinary` in `settings.py`](https://cloudinary.com/blog/managing-media-files-in-django)
- [get the URL with Javascript](https://www.w3schools.com/howto/howto_js_get_url.asp)
- [Bootstrap gutters](https://getbootstrap.com/docs/5.0/layout/gutters/#horizontal-gutters)
- [Bootstrap text utilities](https://getbootstrap.com/docs/5.0/utilities/text/)
- [restrict objects available to staff users in the admin panel](https://stackoverflow.com/a/71318569)
- [Django documentation: `ModelAdmin.get_queryset(request)`](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_queryset)
- [Bootstrap: make all cards the same height](https://stackoverflow.com/questions/35868756/how-to-make-bootstrap-cards-the-same-height-in-card-columns)
- [Bootstrap borders](https://getbootstrap.com/docs/5.0/utilities/borders/)
- [Bootstrap columns](https://getbootstrap.com/docs/5.0/layout/columns/)
- [restrict ForeignKey Field dropdown options in Django admin](https://stackoverflow.com/a/73586108)
- [Django `formfield_for_foreignkey` documentation](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.formfield_for_foreignkey)
- [Bootstrap sizing](https://getbootstrap.com/docs/5.0/utilities/sizing/)
- [preferred way of breaking lines in Python](https://stackoverflow.com/a/53180)
- [built-in error views](https://docs.djangoproject.com/en/4.2/ref/views/)
- [displaying messages based on tags](https://stackoverflow.com/a/16285005)
- [Django messages documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/)
- [`floatformat` template tag](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/) 

### Text

Profile texts for the mockup users based on [Terry Pratchett's Discworld series](https://www.terrypratchettbooks.com/discworld-characters/) were taken from [Wikipedia](https://www.wikipedia.org/). The description of Geoffrey Swivel was adjusted to use the correct pronouns.

All other text was written by me.

[Lemon bar](https://spicy-recipes-django-5d174ffc7c94.herokuapp.com/lemon-bar/) recipe based on [Chili&Vanilia's post](https://chiliesvanilia.blogspot.com/2006/08/amerikai-citromkrmes-szelet-lemon-bar.html).

[Red velvet cake](https://spicy-recipes-django-5d174ffc7c94.herokuapp.com/red-velvet-cake/) recipe based on [Pamela Moxley's post](https://cooking.nytimes.com/recipes/1016333-beet-red-velvet-cake).

### Media

#### Images

[Logo/favicon](https://pixabay.com/illustrations/autism-infinity-symbol-1192408/) by [janeb13](https://pixabay.com/users/janeb13-725943/) on [Pixabay](https://pixabay.com/), converted to `ico` format with [`Favicon.io`](https://favicon.io/favicon-converter/).

All other pictures taken by me.

### Readmes

- [Creating your first README with Kera Cudmore](https://www.youtube.com/watch?v=XbYJ4VlhSnY) by Code Institute
- [Creating your first README](https://github.com/kera-cudmore/readme-examples) by Kera Cudmore
- [Bully Book Club](https://github.com/kera-cudmore/Bully-Book-Club) by Kera Cudmore
- [Bodelschwingher Hof](https://github.com/4n4ru/CI_MS1_BodelschwingherHof/tree/master) by Ana Runje
- [Travel World](https://github.com/PedroCristo/portfolio_project_1/) by Pedro Cristo
- [Sourdough Bakes](https://github.com/siobhanlgorman) by Siobhan Gorman
- [Horizon Photo](https://github.com/Ri-Dearg/horizon-photo/blob/master/README.md#mobile-testing) by Rory Patrick Sheridan
- [BackeStock](https://github.com/amylour/BakeStock/) by [Amy Richardson](https://github.com/amylour)
- [American Pizza Order System](https://github.com/useriasminnaamerican_pizza_order_system/) by [Iasmina Pal](https://github.com/useriasminna)
- [Neverlost](https://github.com/Ri-Dearg/neverlost-thrift) by [Rory Patrick Sheridan](https://github.com/Ri-Dearg)
- [EastStr](https://github.com/ndsurgenor/east-street) by Nathan Surgenor
- [The README of my first Code Institute project](https://github.com/blahosyl/academic-publishing)
- [The README of my second Code Institute project](https://github.com/blahosyl/operator-game)
- [The README of my third Code Institute project](https://github.com/blahosyl/dinner-party)

### Unsolicited pull request by an unknown person

A person unknown to me has forked the project repository and submitted a [pull request](https://github.com/blahosyl/spicy/pull/137) with some code comments added. I had not communicated with this person before this nor asked for their contribution to the repository. The pull request was closed without merging.

### Acknowledgements

I would like to express my deepest gratitude to my mentor, [Rory Patrick Sheridan](https://github.com/Ri-Dearg) for his incredibly useful and understanding support throughout the project.
Issues raised by him or discussed with him can be found [here](https://github.com/blahosyl/spicy/issues?q=label%3Amentor) (see the individual ticket descriptions for the details of his contribution).

I am also grateful to the Code Institute tutoring team, in particular, to John and Roo for their help. The details of their contributions can be found [here](https://github.com/blahosyl/spicy/issues?q=label%3Atutoring).

I would also like to thank Peter Litauszki for photo and video editing help.


