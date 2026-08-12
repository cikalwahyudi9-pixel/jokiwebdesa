// Jelajah Sumberagung — Main JavaScript

document.addEventListener('DOMContentLoaded', function () {

  // =============================================
  // NAVBAR SCROLL EFFECT
  // =============================================
  const navbar = document.getElementById('mainNavbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  }

  // =============================================
  // LIGHTBOX
  // =============================================
  const overlay = document.getElementById('lightboxOverlay');
  const lightboxImg = document.getElementById('lightboxImg');
  const closeBtn = document.getElementById('lightboxClose');

  // Open lightbox on image click
  document.querySelectorAll('[data-lightbox]').forEach(el => {
    el.addEventListener('click', function (e) {
      e.preventDefault();
      const src = this.dataset.lightbox || this.href || this.querySelector('img')?.src;
      const alt = this.dataset.lightboxCaption || this.querySelector('img')?.alt || '';
      if (src && overlay && lightboxImg) {
        lightboxImg.src = src;
        lightboxImg.alt = alt;
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  // Close lightbox
  function closeLightbox() {
    if (overlay) {
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (overlay) {
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeLightbox();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeLightbox();
  });

  // =============================================
  // FILTER BUTTONS (aktif state)
  // =============================================
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', function () {
      // Untuk link filter, Django handle filter via URL param
      // Ini hanya handle active state visual jika filter client-side
    });
  });

  // =============================================
  // SMOOTH SCROLL for anchor links
  // =============================================
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });

  // =============================================
  // GALERI FILTER (client-side jika ada)
  // =============================================
  const galeriItems = document.querySelectorAll('.galeri-item[data-kategori]');
  const galeriFilterBtns = document.querySelectorAll('[data-galeri-filter]');

  if (galeriFilterBtns.length > 0) {
    galeriFilterBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        const filter = this.dataset.galeriFilter;

        galeriFilterBtns.forEach(b => b.classList.remove('active'));
        this.classList.add('active');

        galeriItems.forEach(item => {
          if (filter === 'semua' || item.dataset.kategori === filter) {
            item.style.display = '';
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // =============================================
  // LAZY LOAD images
  // =============================================
  if ('IntersectionObserver' in window) {
    const lazyImages = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
          imageObserver.unobserve(img);
        }
      });
    });

    lazyImages.forEach(img => imageObserver.observe(img));
  }

});
