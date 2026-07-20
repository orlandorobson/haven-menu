(function () {
  const data = window.HAVEN_MENU;
  const target = document.getElementById("printPages");
  const formatPrice = (price) => price.toFixed(3);
  const categories = new Map(data.categories.map((category) => [category.id, category]));

  const renderPrice = (item) => {
    if (!item.largePrice) return `<strong>${formatPrice(item.price)}</strong>`;
    return `
      <strong class="print-size-prices">
        <span><small>Standard</small>${formatPrice(item.price)}</span>
        <span><small>Large</small>${formatPrice(item.largePrice)}</span>
      </strong>`;
  };

  const renderSection = (id) => {
    const category = categories.get(id);
    return `
      <section class="print-section">
        <header>
          <p lang="ar" dir="rtl">${category.arabicName}</p>
          <h2>${category.name}</h2>
        </header>
        ${category.items
          .map(
            (item) => `
              <article>
                <div>
                  <h3>${item.name}</h3>
                  <p lang="ar" dir="rtl">${item.arabicName}</p>
                </div>
                ${renderPrice(item)}
              </article>`
          )
          .join("")}
      </section>`;
  };

  const renderColumn = (ids) =>
    `<div class="print-column">${ids.map(renderSection).join("")}</div>`;

  const renderHeader = (compact = false) => `
    <header class="print-header${compact ? " print-header-compact" : ""}">
      <div>
        <p lang="ar" dir="rtl">هيفن</p>
        <h1>HAVEN</h1>
      </div>
      <span>${compact ? "Menu continued" : "Osara, Salalah"}</span>
    </header>`;

  const renderFooter = () => `
    <footer>
      <span>Prices in OMR</span>
      <span lang="ar" dir="rtl">الأسعار بالريال العماني</span>
    </footer>`;

  target.innerHTML = `
    <section class="sheet">
      ${renderHeader()}
      <section class="photo-strip" aria-label="Haven menu photographs">
        <img src="assets/img/spanish-latte.png" alt="">
        <img src="assets/img/brownie.png" alt="">
        <img src="assets/img/matcha.png" alt="">
      </section>
      <section class="print-menu">
        ${renderColumn(["signature", "black-coffee"])}
        ${renderColumn(["coffee-with-milk"])}
      </section>
      ${renderFooter()}
    </section>
    <section class="sheet">
      ${renderHeader(true)}
      <section class="print-menu print-menu-continuation">
        ${renderColumn(["chocolate-and-specials", "mojitos", "water"])}
        ${renderColumn(["tea", "smoothies-and-shakes", "desserts"])}
      </section>
      ${renderFooter()}
    </section>`;
})();
