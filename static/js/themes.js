const bodyStyles = document.body.style;
let themeSelector = document.getElementById('theme-selector');
// themeSelector.addEventListener('change',changeTheme);

themeSelector.addEventListener("change", getThemeValue);

function getThemeValue() {
    localStorage.setItem("colorTheme", themeSelector.value);
    console.log(localStorage.getItem("colorTheme"));
    
    changeTheme();
}


function changeTheme() {
    const theme = localStorage.getItem("colorTheme");

    document.getElementsByClassName("brand").value = theme;

    if (theme == 'green') {
        bodyStyles.setProperty('--dark-highlight', '#1b871d');
        bodyStyles.setProperty('--highlight', '#7ef075');
        bodyStyles.setProperty('--light-highlight', '#ceedcc');

    }
    else {
        bodyStyles.setProperty('--dark-highlight', '#D7410F');
        bodyStyles.setProperty('--highlight', '#FD7E14');
        bodyStyles.setProperty('--light-highlight', '#f7ddcf');
    }
}