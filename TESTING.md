## HTML validation

### Allauth template: known issue

The allauth template for [`signup.html`](templates/account/signup.html) has a [known issue](https://code-institute-room.slack.com/archives/C026PTF46F5/p1711715226907449) that produces validation errors. Since this is a problem with the framework code, and not the custom code written for this project, and it does not affect the functionality of the app, this was not corrected. 

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
|page loads    |hamburger icon visible||
|page loads    |logo and brand name visible||
|page loads    |nav links not visible||
|page loads    |search bar not visible||
|page loads    |color selector not visible||
|hamburger icon clicked|search bar and color selector revealed||
|hamburger icon clicked again |search bar and color selector hidden||
|logo and brand name clicked|home page loaded||
|color selector changed|page color scheme changes persistently||
|**Search** button clicked |search page loaded||


##### Navigation bar | desktop 

|Action				|Expected result	|Result|
|---				|---				|:---:	|
|page loads    |hamburger icon not visible||
|page loads    |logo and brand name visible||
|page loads    |nav links visible||
|page loads    |search bar visible||
|page loads    |color selector visible||
|logo and brand name clicked|home page loaded||
|color selector changed|page color scheme changes persistently||
|**Search** button clicked |search page loaded||



##### User bar | if user signed in
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|page loads    |"Welcome, `user`!" visible||
|page loads    |"You are not logged in" not visible||
|page loads    |signout link visible||
|signout link clicked|signout page loaded||



##### User bar | if user not signed in
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|page loads    |"Welcome, `user`!" not visible||
|page loads    |"You are not logged in" visible||
|page loads    |signin link visible||
|page loads    |signup link visible||
|signin link clicked|signin page loaded||
|signup link clicked|signup page loaded||

### Footer
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|page loads    |copyright info visible||
|page loads    |GitHub icon visible||
|page loads    |LinkedIn icon visible||
|GitHub icon clicked | GitHub profile opens in new tab||
|LinkedIn icon clicked | LinkedIn profile opens in new tab||

### Home page

|Action				|Expected result	|Result|
|---				|---				|:---:	|
|home page loads    |filters visible||
|home page loads    |recipe list visible||
|filter changed     |filter message visible||
|filter changed     |recipe list is filtered||

### Signin page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|signin page loads    |signin text visible ||
|signin page loads    |signup link visible ||
|signin page loads    |username field visible ||
|signin page loads    |password field visible ||
|signin page loads    |signin button visible ||
|signin page loads    |password reset link visible ||
|signup link clicked|signup page loaded||
|password reset link clicked|password reset page loaded||
|signout button clicked & username field empty |"Please fill in this field"||
|signout button clicked & password field empty |"Please fill in this field"||
|signout button clicked & username & password field not empty & credentials correct |user is signed in||
|signout button clicked & username & password field not empty & credentials correct |home page loads||
|signout button clicked & username & password field not empty & credentials not correct |"The username and/or password you specified are not correct."||



### Signout page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|signout page loads  |signout text n visible||
|signout page loads  |signout button visible||
|signout button clicked  |user signed out||
|signout button clicked  |home page loads||


### Signup page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|signup page loads    | ||

### Email sent page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|email sent page loads    | ||


### Password resent page
|Action				|Expected result	|Result|
|---				|---				|:---:	|
|password reset page loads    | ||
### Recipe detail page

## Accessibility testing

### Lighthouse

### Color contrasts

https://webaim.org/resources/contrastchecker/?fcolor=531D04&bcolor=F7DDCF
https://webaim.org/resources/contrastchecker/?fcolor=0F6895&bcolor=BFE6F7