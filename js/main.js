// main.js - Interactive Features

document.addEventListener('DOMContentLoaded', function() {
  // Navbar scroll effect
  const navbar = document.querySelector('.navbar');
  const menuToggle = document.querySelector('.menu-toggle');
  const navMenu = document.querySelector('.nav-menu');
  
  // Navbar background on scroll
  window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });
  
  // Mobile menu toggle
  if (menuToggle) {
    menuToggle.addEventListener('click', function() {
      menuToggle.classList.toggle('active');
      navMenu.classList.toggle('active');
    });
    
    // Close menu when clicking nav links
    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
      link.addEventListener('click', function() {
        menuToggle.classList.remove('active');
        navMenu.classList.remove('active');
      });
    });
  }
  
  // Smooth scroll for anchor links
  const anchorLinks = document.querySelectorAll('a[href^="#"]');
  anchorLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          const offsetTop = target.offsetTop - 76; // navbar height
          window.scrollTo({
            top: offsetTop,
            behavior: 'smooth'
          });
        }
      }
    });
  });
  
  // Product order buttons
  const orderButtons = document.querySelectorAll('.price button');
  orderButtons.forEach(button => {
    button.addEventListener('click', function() {
      const productCard = this.closest('.product-card');
      const productName = productCard.querySelector('h3').textContent;
      const whatsappNumber = '6285880880476';
      const message = encodeURIComponent(`Halo! Saya tertarik dengan ${productName}. Bisa info lebih lanjut?`);
      const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${message}`;
      window.open(whatsappUrl, '_blank');
    });
  });
  
  // Intersection Observer for fade-in animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);
  
  // Observe elements for animation
  const animateElements = document.querySelectorAll('.product-card, .service-card, .testimonial-card, .stat-box');
  animateElements.forEach((el, index) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
    observer.observe(el);
  });
  
  // Stats counter animation
  const statNumbers = document.querySelectorAll('.stat-box h3');
  let hasAnimated = false;
  
  const statsObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting && !hasAnimated) {
        hasAnimated = true;
        statNumbers.forEach(stat => {
          const text = stat.textContent;
          const number = parseInt(text.replace(/\D/g, ''));
          const suffix = text.replace(/[\d.]/g, '');
          
          if (!isNaN(number)) {
            animateCounter(stat, 0, number, suffix, 2000);
          }
        });
      }
    });
  }, { threshold: 0.5 });
  
  const statsSection = document.querySelector('.stats');
  if (statsSection) {
    statsObserver.observe(statsSection);
  }
  
  function animateCounter(element, start, end, suffix, duration) {
    const range = end - start;
    const increment = range / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
      current += increment;
      if (current >= end) {
        element.textContent = end + suffix;
        clearInterval(timer);
      } else {
        element.textContent = Math.floor(current) + suffix;
      }
    }, 16);
  }
  
  // Add hover sound effect (optional, disabled by default)
  // Uncomment to enable button hover sounds
  /*
  const buttons = document.querySelectorAll('button, .btn-primary, .btn-secondary');
  buttons.forEach(button => {
    button.addEventListener('mouseenter', function() {
      // Play subtle hover sound
      // const audio = new Audio('assets/hover.mp3');
      // audio.volume = 0.2;
      // audio.play().catch(() => {});
    });
  });
  */
});

// Performance optimization: Lazy load images
if ('IntersectionObserver' in window) {
  const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        if (img.dataset.src) {
          img.style.backgroundImage = `url(${img.dataset.src})`;
          imageObserver.unobserve(img);
        }
      }
    });
  });
  
  // Observe product images for lazy loading
  document.querySelectorAll('.product-img[data-src]').forEach(img => {
    imageObserver.observe(img);
  });
}
