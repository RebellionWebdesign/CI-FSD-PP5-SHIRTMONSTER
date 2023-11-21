document.addEventListener("DOMContentLoaded", function () {
    /* This snippet is required to render the Lucide Icons -> https://lucide.dev/guide/packages/lucide */
    lucide.createIcons();

    /* Checks if the url is one of the login/logout/password urls and hides the header */
    let loginUrl = window.location.href.includes('login');
    let logoutUrl = window.location.href.includes('logout');
    let signupUrl = window.location.href.includes('signup');
    let resetUrl = window.location.href.includes('reset');
    const header = document.getElementById('header')
    const search = document.getElementById('search-box')

    if (loginUrl) {
        header.classList.add("hide");
        search.classList.add("hide");
    } else if (logoutUrl) {
        header.classList.add("hide");
        search.classList.add("hide");
    } else if (signupUrl) {
        header.classList.add("hide");
        search.classList.add("hide");
    } else if (resetUrl) {
        header.classList.add("hide");
        search.classList.add("hide");
    }

    /* Custom settings for the bootstrap carousel -> https://getbootstrap.com/docs/4.6/components/carousel/ */
    $('.carousel').carousel({
        interval: 5000,
        touch: true,
    })

    /* Looks for the mobile menu classes */
    const mobileToggleOpen = document.getElementsByClassName("mobile-open")[0]
    const mobileToggleClose = document.getElementsByClassName("mobile-close")[0]
    const navBar = document.getElementsByClassName("mobile-menu")[0]
    /* Looks for the search box classes */
    const searchToggleOpen = document.getElementsByClassName("search-toggle")[0]
    const searchToggleClose = document.getElementsByClassName("close-toggle")[0]
    const searchBox = document.getElementsByClassName("search-box")[0]

    /* Opens the search box and changes the icon*/
    searchToggleOpen.addEventListener("click", () => {
        searchBox.classList.remove("closed-search")
        searchBox.classList.add("open-search")
        searchToggleOpen.classList.add("d-none")
        searchToggleClose.classList.remove("d-none")

    })

    /* Closes the search box and changes the icon*/
    searchToggleClose.addEventListener("click", () => {
        searchBox.classList.remove("open-search")
        searchBox.classList.add("closed-search")
        searchToggleOpen.classList.remove("d-none")
        searchToggleClose.classList.add("d-none")
    })

    /* Opens the mobile slide out menu and closes the search box*/
    mobileToggleOpen.addEventListener("click", () => {
        navBar.classList.remove("closed")
        navBar.classList.add("open")
        searchBox.classList.remove("open-search")
        searchBox.classList.add("closed-search")
    })

    //This does exactly the same as above, only with the close icon inside the sidebar and of course the other way around.
    mobileToggleClose.addEventListener("click", () => {
        navBar.classList.remove("open")
        navBar.classList.add("closed")
        searchBox.classList.remove("open-search")
        searchBox.classList.add("closed-search")
        searchToggleOpen.classList.remove("d-none")
        searchToggleClose.classList.add("d-none")
    })

})
