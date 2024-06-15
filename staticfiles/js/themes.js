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

/** check if storage is already populated */
function checkStorage() {
    if(!localStorage.getItem('theme-selector')) {
        storeColorTheme();
    } else {
        setColorTheme();
    }
}

/** populate storage with the value form the color theme selector form */
function storeColorTheme() {
    localStorage.setItem("colorTheme", themeSelector.value);
    console.log(localStorage.getItem("colorTheme"));
    
    setColorTheme();
}

/** set the site's color theme based on the value in storage */
function setColorTheme() {
    // get the theme value from storage
    let currentTheme = localStorage.getItem("colorTheme");

    // set the theme selector value to the one retrieved from storage
    themeSelector.value = currentTheme;

    // set the CSS color variables depending on the selected theme

    if (currentTheme == 'orange') {
        bodyStyles.setProperty('--dark-highlight', '#D7410F');
        bodyStyles.setProperty('--highlight', '#FD7E14');
        bodyStyles.setProperty('--light-highlight', '#f7ddcf');
    }

    else if (currentTheme == 'green') {
        bodyStyles.setProperty('--dark-highlight', '#1b871d');
        bodyStyles.setProperty('--highlight', '#7ef075');
        bodyStyles.setProperty('--light-highlight', '#ceedcc');
    }
    else if (currentTheme == 'blue') {
        bodyStyles.setProperty('--dark-highlight', 'darkblue');
        bodyStyles.setProperty('--highlight', 'blue');
        bodyStyles.setProperty('--light-highlight', 'lightblue');

    }
    // default is also orange
    else {
        bodyStyles.setProperty('--dark-highlight', '#D7410F');
        bodyStyles.setProperty('--highlight', '#FD7E14');
        bodyStyles.setProperty('--light-highlight', '#f7ddcf');
    }
}

themeSelector.addEventListener("change", storeColorTheme);
document.addEventListener("DOMContentLoaded", setColorTheme)