// This script lets the user choose between pre-defined color themes
// using the drop-down form in the nav bar

// The selected theme value is stored in local storage, so it persists
// across tabs & windows

// Code based on the Mozilla Web Storage API tutorial:
// https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API

// Using session storage for this functionality was suggested
// by my mentor, Rory Patrick Sheridan: https://github.com/Ri-Dearg


// get body style – CSS color variables are defined in the root
const bodyStyles = document.body.style;
// get the color theme selector dropdown form
let themeSelector = document.getElementById('theme-selector');
// get the locally stored color theme value (if any)
let currentTheme = localStorage.getItem("colorTheme")

/** populate storage with the value form the color theme selector form */
function storeColorTheme() {
    console.log("storeColorTheme");
    localStorage.setItem("colorTheme", themeSelector.value);
    console.log(localStorage.getItem("colorTheme"));
    
    setColorTheme();
}

/** set the site's color theme based on the value in storage */
function setColorTheme() {
    console.log("setColorTheme");
    // if there is no stored value, default to orange
    if (!localStorage.getItem("colorTheme")) {
        console.log("setColorTheme: default to orange");
        currentTheme = 'orange';
    } else {
        // get the theme value from storage
        console.log("setColorTheme: get value from storage");
        currentTheme = localStorage.getItem("colorTheme");
    }

    // set the theme selector value to the one retrieved from storage
    themeSelector.value = currentTheme;

    // set the CSS color variables depending on the selected theme

    if (currentTheme) {
        bodyStyles.setProperty('--very-dark-highlight', 'var(--very-dark-' + currentTheme + ')');
        bodyStyles.setProperty('--dark-highlight', 'var(--dark-' + currentTheme + ')');
        bodyStyles.setProperty('--highlight', 'var(--med-' + currentTheme + ')');
        bodyStyles.setProperty('--light-highlight', 'var(--light-' + currentTheme + ')');
        }

    // default is orange
    else {
        bodyStyles.setProperty('--very-dark-highlight', 'var(--very-dark-orange)');
        bodyStyles.setProperty('--dark-highlight', 'var(--dark-orange)');
        bodyStyles.setProperty('--highlight', 'var(--med-orange)');
        bodyStyles.setProperty('--light-highlight', 'var(--light-orange)');
    }
}

themeSelector.addEventListener("change", storeColorTheme);
document.addEventListener("DOMContentLoaded", setColorTheme);