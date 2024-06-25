## HTML validation

### Allauth template: known issue

The allauth template for [`Signup.html`](templates/account/Signup.html) has a [known issue](https://code-institute-room.slack.com/archives/C026PTF46F5/p1711715226907449) that produces validation errors. Since this is a problem with the framework code, and not the custom code written for this project, and it does not affect the functionality of the app, this was not corrected. 

## JavaScript validation

### `comments.js`: known issue

The file `comments.js` (which is identical to [the one used in the walkthrough project](https://github.com/Code-Institute-Solutions/blog/blob/main/15_testing/static/js/comments.js)) produces the following error during JS validation:

```
1 undefined variable
bootstrap
```

![JavaScript validation error: unknown variable `bootstrap`](testing/code-validation/js-validation/js-validation-known-error-bootstrap.png)

## Manual feature testing

### Navigation bar

##### Navigation bar | mobile 

|Action				|Expected result	|Result|
|---				|---				|:---:	|
|page loads    |hamburger icon visible<br>logo and brand name visible<br>brand text not visible<br>nav links not visible<br>Search bar not visible<br>color selector not visible||
|hamburger icon clicked|Search bar and color selector revealed||
|hamburger icon clicked again |Search bar and color selector hidden||
|logo and brand name clicked|[home page](#home-page) loaded||
|color selector changed|page color scheme changes persistently||
|**Search** button clicked |[Search page](#Search-results-page) loaded||


##### Navigation bar | desktop 

|Action				|Expected result	|Result|
|---				|---				|:---:	|
|page loads    |hamburger icon not visible<br>logo and brand name visible<br>brand text visible<br>nav links visible<br>Search bar visible<br>color selector visible||
|logo and brand name clicked|[home page](#home-page) loaded||
|color selector changed|page color scheme changes persistently||
|**Search** button clicked |[Search page](#Search-results-page) loaded||



##### User bar | if user signed in
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|page loads    |"Welcome, `user`!" visible<br>"You are not logged in" not visible<br>Signout link visible||
|Signout link clicked|[Signout page](#Signout-page) loaded||



##### User bar | if user not signed in
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|page loads    |"Welcome, `user`!" not visible<br>"You are not logged in" visible<br>Signin link visible<br>||
|Signin link clicked|[Signin page](#Signin-page) loaded||
|Signup link clicked|[Signup page](#Signup-page) loaded||

### Footer
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|page loads    |copyright info visible<br>GitHub icon visible<br>LinkedIn icon visible||
|GitHub icon clicked | GitHub profile opens in new tab||
|LinkedIn icon clicked | LinkedIn profile opens in new tab||

### Home page

|Action				|Expected result	|Result|
|---				|---				|:---:	|
|home page loads    |filters visible<br>recipe cards visible<br>pagination visible||
|any recipe card clicked|corresponding [recipe detail page](#recipe-detail-page) loads||
|filter changed     |result count visible<br>recipe list is filtered||
|result count > 6   |[pagination](#pagination-links) visible||

### Recipe detail page

|Action				|Expected result	|Result|
|---				|---				|:---:	|
|recipe detail page loads|title visible<br>author visible<br>attributes visible (if any)<br>ingedients visible (if any)<br>image visible<br>total time, prep time & cook time visible<br>instructions visible<br>comments visible (if any)||
|user not logged in|"Sign in to leave a comment"||
|user logged in|comment field visible<br>comment field & button visible<br>own pending comments visible||
|user logged in<br>user has comments|Edit & Delete button visible for each comment<br>||
|comment button clicked<br>comment field empy|"Please fill in this field"||
|comment button clicked<br>comment field not empy|comment appears as unapproved<br>edit & delete buttons appear||
|Edit button clicked|comment text filled into comment field<br>Submit button changes to Update||
|Update button clicked|comment text updated<br>comment set to unapproved||
|Delete button clicked|delete modal pops up||
|Delete button on delete modal |delete modal closes<br>comment remains||
|Delete button clicked on delete modal|comment is deleted<br>confirmation message appears||


### Community page

|Action				|Expected result	|Result|
|---				|---				|:---:	|
|Community page loads  |profile cards visible||
|any profile card clicked|corresponding [profile detail page](#profile-detail-page) loads||

### Profile detail page

|Action				|Expected result	|Result|
|---				|---				|:---:	|
|Profile detail page loads|name or username visible<br>status visible<br>pronouns visible (if any)<br>neurodiversity visible (if any)<br>about text visible (if any)||

### Search results page

|Action				|Expected result	|Result|
|---				|---				|:---:	|
|Search page loaded |result count visible<br>recipe list is filtered||
|result count > 6   |[pagination](#pagination-links) visible||

### Pagination links
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|more recipes/results exist |**Next** button visible||
|previous results exist |**Prev** button visible||
|**Next** button clicked |next page of results is loaded||
|**Prev** button clicked |previous page of results is loaded||


### Signin page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|Signin page loads    |Signin text visible<br>Signup link visible<br>username field visible<br>password field visible<br>Signup button visible<br>password reset link visible||
|Signup link clicked|[Signup page](#Signup-page) loaded||
|password reset link clicked|[password reset page](#password-reset-page) loaded||
|Signin button clicked<br>any field empty |"Please fill in this field"||
|Signin button clicked<br>noth fields filled<br>credentials not correct|"The username and/or password you specified are not correct."||
|Signin button clicked<br>both fields filled<br>credentials correct<br>email not confirmed |user is signed in<br>[Email sent page](#email-sent-page) loads<br>confirmation email sent||
|Signin button clicked<br>both fields filled<br>credentials correct<br>email confirmed|user is signed in<br>[home page](#home-page) loads||

### Signout page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|Signout page loads  |Signout text visible<br>Signout button visible||
|Signout button clicked  |user signed out<br>home page loads||


### Signup page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|Signup page loads    |Signup text visible<br>Signin link visible<br>email filed visible<br>username field visible<br>password field visible<br>password rules visible<br>password (again) field visible<br>Signup button visible<br>password reset link visible||
|Signin link clicked|[Signin page](#Signin-page) loaded||
|password reset link clicked|[password reset page](#password-reset-page) loaded||
|Signup button clicked<br>any field empty |"Please fill in this field"||
|Signup button clicked<br>email field has no `@`|"Please include an `@`..."||
|Signup button clicked<br>password fields don't match<br>OR password does not conform to rules |password fields get emptied||
|Signup button clicked<br>email already registered|"A user with that username already exists"||
|Signup button clicked<br>all fields filled correctly |user is signed up<br>[Email sent page](#email-sent-page) loads<br>verification email sent to user||
|user clicks link in verification email|[Confirm email page](#confirm-email-page) loads|


### Email sent page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|Email sent page loads    |confirmation email sent to user||

### Confirm email page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|Confirm email page loads|confirm text visible<br>confirm button visible<br> ||
|confirm button clicked    |resitration confirmed<br>[Signin page](#Signin-page) loads||

### Password reset page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|password reset page loads |reset text visible<br>email field visible<br>reset button visible||
|reset button clicked<br>email not valid|"email not valid"|
|reset button clicked<br>email valid<br>email not in database|reset confirmation page loads<br>"we have no record of you" email sent||
|reset button clicked<br>email valid<br>email in database|reset confirmation page loads<br>password reset email sent||
|reset link in email clicked|[change password page](#change-password-page) shown||

### Change password page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|change password loads|change password text visible<br>new password field visible<br>new password again field visible<br>change pasword button visible<br> ||
|change pasword button clicked<br>passwords match|"Your password is now changed"||

## Accessibility testing

### Lighthouse

### Color contrasts

https://webaim.org/resources/contrastchecker/?fcolor=531D04&bcolor=F7DDCF
https://webaim.org/resources/contrastchecker/?fcolor=0F6895&bcolor=BFE6F7

## Bugs

All bugs are tracked in [GitHub Issues](https://github.com/blahosyl/spicy/issues?q=is%3Aissue+label%3Abug).

#### Known bugs

Known bugs are listed in [GitHub Issues](https://github.com/blahosyl/spicy/issues?q=is%3Aissue+label%3Abug+is%3Aopen).

#### Solved bugs

Solved bugs are listed in [GitHub Issues](https://github.com/blahosyl/spicy/issues?q=is%3Aissue+label%3Abug+is%3Aclosed).