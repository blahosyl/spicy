
## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

## UX

## Design

### Data models

#### Recipe

Partially based on the Post model of the I Think Therefore I Blog walkthrough, but changed several aspects:

- Published is Boolean
- Separated content into
	- Instructions
	- PrepTime
	- CookTime
	- Ingredients (separate table)

#### Ingredient

##### 2 tables for ingredients

- Ingredient: lists ingredients, global list
- IngredientQueantity: connects ingredients with recipes, has unit and quantity attributes. Even if there are 2 recipes that call for 2 apples each, these are treated as separate entities.


##### Quantity data type

[Decimal](https://docs.python.org/3/library/decimal.html#module-decimal) instead of float used for quantity.

##### IngredientQuantity not compulsory

Recipes can be saved without any ingredients (at least for a draft).

Maybe add check to see if a recipe has at least 1 ingredient before publishing?

##### Instances of Ingredient cannot be duplicated

Instances of ingredient where `ingr_name` & `preparation` is the same cannot be duplicated. 

- "cheese, sliced" and "cheese, grated" are both possible
- 2 instances of "cheese, grated" are not allowed

This is true when added new ingredients as well as when editing exisitng one would result in a duplicated.

##### IngredientQuantities **can** be duplicated

#### Comment

Based entirely on the Comment model of the I Think Therefore I Blog walkthrough.

## Features

## Technoogies used

### Languages & frameworks used

### Tools used

### Deveopment process

## Depoyment

## Testing

See the document [`TESTING.md`](TESTING.md) for details.

## Credits

### Study/lookup cources


- [Show labels and Milestones in GitHub Projects Kanban board](https://github.com/orgs/community/discussions/10788)
- [Creating and editing milestones for issues and pull requests](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/creating-and-editing-milestones-for-issues-and-pull-requests)
- [making a model for ingredients](https://groups.google.com/g/django-users/c/DtkxblwqWbE/m/zJfqURzgxkUJ)
- [connector types in Entity Relationship Diagrams](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning)
- [float vs. decimal in Python](https://docs.python.org/3/library/decimal.html#module-decimal)
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
- [Attribute error (missing) caused by indentation error in `views.py`](https://stackoverflow.com/a/64709139)

### General advice

- Daisy McGirr: allauth social option
- Leon Potgieter: Neon DB, help with [testing on local DB issue](https://code-institute-room.slack.com/archives/C02B3MJQABA/p1716915411743489?thread_ts=1716855535.547499&cid=C02B3MJQABA)



### Code credits

### Content

### Media

#### Images

### Readme

### Readme

- [Creating your first README with Kera Cudmore](https://www.youtube.com/watch?v=XbYJ4VlhSnY) by Code Institute
- [Creating your first README](https://github.com/kera-cudmore/readme-examples) by Kera Cudmore
- [Bully Book Club](https://github.com/kera-cudmore/Bully-Book-Club) by Kera Cudmore
- [Bodelschwingher Hof](https://github.com/4n4ru/CI_MS1_BodelschwingherHof/tree/master) by Ana Runje
- [Travel World](https://github.com/PedroCristo/portfolio_project_1/) by Pedro Cristo
- [Sourdough Bakes](https://github.com/siobhanlgorman) by Siobhan Gorman
- [Horizon Photo](https://github.com/Ri-Dearg/horizon-photo/blob/master/README.md#mobile-testing) by Rory Patrick Sheridan
- [BackeStock](https://github.com/amylour/BakeStock/) by [Amy Richardson](https://github.com/amylour)
- [American Pizza Order System](https://github.com/useriasminnaamerican_pizza_order_system/) by [Iasmina Pal](https://github.com/useriasminna)
- [The README of my first Code Institute project](https://github.com/blahosyl/academic-publishing)
- [The README of my second Code Institute project](https://github.com/blahosyl/operator-game)
- [The README of my third Code Institute project](https://github.com/blahosyl/dinner-party)




