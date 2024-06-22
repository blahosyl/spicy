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

Color contrasts

https://webaim.org/resources/contrastchecker/?fcolor=531D04&bcolor=F7DDCF
https://webaim.org/resources/contrastchecker/?fcolor=0F6895&bcolor=BFE6F7