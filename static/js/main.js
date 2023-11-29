document.addEventListener("DOMContentLoaded", function () {

    // Generate lucide icons
    lucide.createIcons();

    // Here we initialize swiper js
    const swiper = new Swiper('.swiper', {
        // Optional parameters
        direction: 'horizontal',
        loop: true,

        autoplay: {
            delay: 5000,
            disableOnInteraction: true,
        },

        // If we need pagination
        pagination: {
            el: '.swiper-pagination',
            dynamicBullets: true,
        },

        // Navigation arrows
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },

        // And if we need a scrollbar
        scrollbar: {
            el: '.swiper-scrollbar',
        },
    });

    // This opens the search bar on mobile screens
    const searchToggleOpen = document.getElementById("mobile-search-open")
    const searchToggleClose = document.getElementById("mobile-search-close")
    const searchBox = document.getElementById("search-box")

    searchToggleOpen.addEventListener("click", () => {
        searchBox.style.display = "flex"
        searchToggleOpen.classList.add("hide")
        searchToggleClose.classList.remove("hide")
    
    })

    // This closes the search bar on mobile screens
    searchToggleClose.addEventListener("click", () => {
        searchBox.style.display = "none"
        searchToggleOpen.classList.remove("hide")
        searchToggleClose.classList.add("hide")
    
    })

    //This opens the sorting menu on click
    const sortToggleOpen = document.getElementById("sort-open")
    const sortLink = document.getElementsByClassName("sort-link")
    const sortBox = document.getElementById("sort-box")

    sortToggleOpen.addEventListener("click", () => {
        sortBox.classList.remove("hide")

    })

})
