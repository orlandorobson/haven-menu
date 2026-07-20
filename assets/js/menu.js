(function () {
  const data = window.HAVEN_MENU;
  const homeEl = document.getElementById("home");
  const chapterViewEl = document.getElementById("chapterView");
  const heroEl = document.getElementById("chapterHero");
  const chapterIndexEl = document.getElementById("chapterIndex");
  const chapterTitleEl = document.getElementById("chapterTitle");
  const chapterArabicEl = document.getElementById("chapterArabic");
  const subcategoryNavEl = document.getElementById("subcategoryNav");
  const menuEl = document.getElementById("menu");

  const chapters = [
    {
      id: "hot",
      index: "Chapter 01",
      name: "Hot Drinks",
      arabicName: "المشروبات الساخنة",
      image: "assets/img/haven-spanish-latte-web.jpg",
      imagePosition: "center 58%",
      matches: (item) => item.tags.includes("Hot")
    },
    {
      id: "iced",
      index: "Chapter 02",
      name: "Iced Drinks",
      arabicName: "المشروبات الباردة",
      image: "assets/img/haven-matcha-real.jpg",
      imagePosition: "center 58%",
      matches: (item) => item.tags.includes("Iced") || item.tags.includes("Cold"),
      spotlight: {
        itemId: "karkade",
        label: "Made at Haven",
        image: "assets/img/haven-karkade-real.jpg"
      }
    },
    {
      id: "sweets",
      index: "Chapter 03",
      name: "Sweets & Desserts",
      arabicName: "الحلويات",
      image: "assets/img/haven-brownie-web.jpg",
      imagePosition: "center 52%",
      matches: (item) => item.tags.includes("Dessert")
    }
  ];

  const formatPrice = (price) => price.toFixed(3);

  function renderPrice(item) {
    if (!item.largePrice) {
      return `
        <strong class="item-price" aria-label="${formatPrice(item.price)} OMR">
          <span>${formatPrice(item.price)}<small>OMR</small></span>
        </strong>`;
    }

    return `
      <strong class="item-price has-sizes" aria-label="Standard ${formatPrice(item.price)} OMR, large ${formatPrice(item.largePrice)} OMR">
        <span><small>Standard</small>${formatPrice(item.price)}</span>
        <span><small>Large</small>${formatPrice(item.largePrice)}</span>
        <i>OMR</i>
      </strong>`;
  }

  function groupedItems(chapter) {
    return data.categories
      .map((category) => ({
        category,
        items: category.items.filter(chapter.matches)
      }))
      .filter((group) => group.items.length);
  }

  function renderItem(item) {
    return `
      <article class="menu-item">
        <div>
          ${item.label ? `<p class="item-label">${item.label} <span lang="ar" dir="rtl">${item.arabicLabel}</span></p>` : ""}
          <div class="item-name">
            <h4>${item.name}</h4>
            <p lang="ar" dir="rtl">${item.arabicName}</p>
          </div>
          <p class="item-description">${item.description}</p>
          <p class="item-description item-description-ar" lang="ar" dir="rtl">${item.arabicDescription}</p>
        </div>
        ${renderPrice(item)}
      </article>`;
  }

  function renderSpotlight(chapter, item) {
    if (!chapter.spotlight || chapter.spotlight.itemId !== item.id) return "";
    return `
      <aside class="spotlight" style="background-image: url('${chapter.spotlight.image}')">
        <div>
          <p>${chapter.spotlight.label}</p>
          <h3>${item.name}</h3>
          <span lang="ar" dir="rtl">${item.arabicName}</span>
        </div>
      </aside>`;
  }

  function renderChapter(chapter) {
    const groups = groupedItems(chapter);

    chapterIndexEl.textContent = chapter.index;
    chapterTitleEl.textContent = chapter.name;
    chapterArabicEl.textContent = chapter.arabicName;
    heroEl.style.backgroundImage = `url('${chapter.image}')`;
    heroEl.style.backgroundPosition = chapter.imagePosition;

    subcategoryNavEl.innerHTML = groups
      .map(
        ({ category }) =>
          `<button type="button" data-target="${chapter.id}-${category.id}">${category.name}</button>`
      )
      .join("");

    menuEl.innerHTML = groups
      .map(
        ({ category, items }) => `
          <section class="menu-section" id="${chapter.id}-${category.id}">
            <header class="section-heading">
              <h3>${category.name}</h3>
              <p lang="ar" dir="rtl">${category.arabicName}</p>
            </header>
            ${items
              .map((item) => `${renderSpotlight(chapter, item)}${renderItem(item)}`)
              .join("")}
          </section>`
      )
      .join("");
  }

  function showHome() {
    document.body.classList.remove("chapter-open");
    homeEl.hidden = false;
    chapterViewEl.hidden = true;
    document.title = "Haven Cafe Menu | Osara, Salalah";
    window.scrollTo(0, 0);
  }

  function showChapter(chapter) {
    renderChapter(chapter);
    document.body.classList.add("chapter-open");
    homeEl.hidden = true;
    chapterViewEl.hidden = false;
    document.title = `${chapter.name} | Haven Cafe`;
    window.scrollTo(0, 0);
  }

  function route() {
    const routeId = window.location.hash.replace("#", "");
    const chapter = chapters.find((candidate) => candidate.id === routeId);
    if (chapter) showChapter(chapter);
    else showHome();
  }

  subcategoryNavEl.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-target]");
    if (!button) return;
    document.getElementById(button.dataset.target)?.scrollIntoView();
  });

  window.addEventListener("hashchange", route);
  route();
})();
