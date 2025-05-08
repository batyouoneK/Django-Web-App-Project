/**
 * Main JavaScript file for CV Website
 * Enhanced interactions and animations
 * Version 2.0
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components when document is ready
    initializeSkillBars();
    initializeSmoothScrolling();
    setActiveNavItem();
    enhanceProjectCards();
    animateTimelineItems();
    
    // Handle project filters if on projects page
    const filterButtons = document.querySelectorAll('.filter-btn');
    if (filterButtons.length > 0) {
        initializeProjectFilters();
    }
    
    // Handle scroll-to-top button
    initializeScrollToTop();
});

/**
 * Initializes and animates skill bars based on data-percentage attributes
 * Enhanced with better animations and mobile support
 */
function initializeSkillBars() {
    const skillBars = document.querySelectorAll('.skill-percentage');
    
    if (skillBars.length === 0) return;
    
    // Process all skill bars
    skillBars.forEach(bar => {
        // Get percentage value from data attribute
        const percentageValue = bar.getAttribute('data-percentage');
        if (percentageValue) {
            // Initially set width to 0 for animation
            bar.style.width = '0%';
            
            // Add the actual percentage value for immediate mobile display
            if (window.innerWidth < 768) {
                bar.style.width = percentageValue + '%';
            }
        }
    });
    
    // Function to check if element is in viewport
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        const buffer = 100; // Start animation a bit before element enters viewport
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) + buffer &&
            rect.bottom >= 0 &&
            rect.left <= (window.innerWidth || document.documentElement.clientWidth) + buffer &&
            rect.right >= 0
        );
    }
    
    // Animate skill bars when they come into view
    function animateSkillBars() {
        skillBars.forEach(bar => {
            // Get percentage from data attribute
            const percentageValue = bar.getAttribute('data-percentage');
            
            if (percentageValue && isInViewport(bar.parentElement)) {
                setTimeout(() => {
                    bar.style.width = percentageValue + '%';
                }, 100);
            }
        });
    }
    
    // Run on scroll with throttling for performance
    let isScrolling;
    window.addEventListener('scroll', function() {
        // Clear the timeout if it's set
        window.clearTimeout(isScrolling);
        
        // Set a timeout to run animateSkillBars after scrolling stops
        isScrolling = setTimeout(animateSkillBars, 50);
    });
    
    // Run once on page load with a slight delay
    setTimeout(animateSkillBars, 500);
}

/**
 * Adds smooth scrolling to anchor links
 */
function initializeSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (!targetElement) return;
            
            // Get header height for offset (with some extra padding)
            const headerHeight = document.querySelector('.site-header')?.offsetHeight || 0;
            const offsetTop = targetElement.offsetTop - headerHeight - 20;
            
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
            
            // Update URL without reload
            history.pushState(null, null, targetId);
        });
    });
}

/**
 * Sets the active navigation item based on current URL or scroll position
 */
function setActiveNavItem() {
    const navItems = document.querySelectorAll('.nav-link');
    const currentPath = window.location.pathname;
    const sections = document.querySelectorAll('section[id]');
    
    // First set active based on URL
    navItems.forEach(item => {
        const href = item.getAttribute('href');
        if (href && (href === currentPath || currentPath.includes(href.split('#')[0]))) {
            document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
            item.classList.add('active');
        }
    });
    
    // Then update active nav based on scroll position
    if (sections.length > 0) {
        window.addEventListener('scroll', function() {
            let currentSection = '';
            const scrollPosition = window.scrollY + 100; // Add offset
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.offsetHeight;
                
                if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                    currentSection = section.getAttribute('id');
                }
            });
            
            navItems.forEach(item => {
                item.classList.remove('active');
                const href = item.getAttribute('href');
                if (href && href.includes(`#${currentSection}`)) {
                    item.classList.add('active');
                }
            });
        });
    }
}

/**
 * Enhance project card interactions
 */
function enhanceProjectCards() {
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        // Add hover effect
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px)';
            this.style.boxShadow = '0 20px 40px rgba(0, 0, 0, 0.6), 0 0 25px rgba(52, 152, 219, 0.5)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '';
        });
    });
}

/**
 * Animate timeline items on scroll
 */
function animateTimelineItems() {
    const timelineItems = document.querySelectorAll('.timeline-item');
    
    if (timelineItems.length === 0) return;
    
    // Function to check if element is in viewport
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        const buffer = 150; // Start animation before fully in viewport
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) + buffer &&
            rect.bottom >= 0
        );
    }
    
    // Function to animate timeline items
    function animateTimeline() {
        timelineItems.forEach((item, index) => {
            if (isInViewport(item) && !item.classList.contains('animated')) {
                setTimeout(() => {
                    item.classList.add('animated');
                    item.style.transform = 'translateX(10px) translateY(-5px)';
                    item.style.opacity = '1';
                }, index * 200); // Stagger the animations
            }
        });
    }
    
    // Set initial styles
    timelineItems.forEach(item => {
        item.style.transform = 'translateX(0) translateY(0)';
        item.style.opacity = '0.6';
        item.style.transition = 'transform 0.5s ease, opacity 0.5s ease, box-shadow 0.5s ease';
    });
    
    // Run on scroll
    window.addEventListener('scroll', animateTimeline);
    
    // Run once on page load
    setTimeout(animateTimeline, 500);
}

/**
 * Initialize scroll to top button
 */
function initializeScrollToTop() {
    // Create button element
    const scrollBtn = document.createElement('button');
    scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollBtn.className = 'scroll-to-top';
    scrollBtn.title = 'Scroll to Top';
    
    // Style the button
    scrollBtn.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        visibility: hidden;
        transition: all 0.4s ease;
        z-index: 1000;
    `;
    
    // Add the button to the document
    document.body.appendChild(scrollBtn);
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) { // Show after scrolling 300px
            scrollBtn.style.opacity = '1';
            scrollBtn.style.visibility = 'visible';
        } else {
            scrollBtn.style.opacity = '0';
            scrollBtn.style.visibility = 'hidden';
        }
    });
    
    // Scroll to top on click
    scrollBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/**
 * Initializes project filtering functionality
 */
function initializeProjectFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectItems = document.querySelectorAll('.project-item');
    const searchInput = document.getElementById('projectSearch');
    
    // Filter function that combines button filters and search text
    function filterProjects() {
        const activeFilter = document.querySelector('.filter-btn.active').getAttribute('data-filter');
        const searchText = searchInput ? searchInput.value.toLowerCase() : '';
        let visibleCount = 0;
        
        projectItems.forEach(item => {
            const matchesFilter = activeFilter === 'all' || item.classList.contains(activeFilter);
            const matchesSearch = !searchText || 
                item.querySelector('.card-title').textContent.toLowerCase().includes(searchText) ||
                item.querySelector('.card-text').textContent.toLowerCase().includes(searchText);
            
            if (matchesFilter && matchesSearch) {
                item.style.display = 'block';
                visibleCount++;
                
                // Add fade-in animation
                item.classList.add('fade-in');
            } else {
                item.style.display = 'none';
                item.classList.remove('fade-in');
            }
        });
        
        // Show message when no results
        const noResults = document.getElementById('noResultsMessage');
        if (noResults) {
            noResults.style.display = visibleCount === 0 ? 'block' : 'none';
        }
    }
    
    // Add click event to filter buttons with animation
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Update active class
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Animate button
            this.style.transform = 'translateY(-3px)';
            setTimeout(() => {
                this.style.transform = '';
            }, 300);
            
            // Apply filters with slight delay for button animation
            setTimeout(filterProjects, 100);
        });
    });
    
    // Add keyup event to search input with debouncing
    if (searchInput) {
        let debounceTimer;
        searchInput.addEventListener('keyup', function() {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(filterProjects, 300);
        });
    }
}