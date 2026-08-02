(function () {
  const data = window.HAVEN_MENU;
  const target = document.getElementById("printPages");
  const formatPrice = (price) => price.toFixed(3);
  const currencySign = '<span class="omr-sign" aria-hidden="true"></span>';
  const categories = new Map(data.categories.map((category) => [category.id, category]));

  const renderPrice = (item) => {
    if (!item.largePrice) {
      return `<strong class="print-price" aria-label="${formatPrice(item.price)} OMR">${currencySign}${formatPrice(item.price)}</strong>`;
    }
    return `
      <strong class="print-size-prices" aria-label="Standard ${formatPrice(item.price)} OMR, large ${formatPrice(item.largePrice)} OMR">
        <span><small>Standard</small><b>${currencySign}${formatPrice(item.price)}</b></span>
        <span><small>Large</small><b>${currencySign}${formatPrice(item.largePrice)}</b></span>
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
                  ${item.label ? `<span class="print-label">${item.label}</span>` : ""}
                  <h3>${item.name}</h3>
                  <p lang="ar" dir="rtl">${item.arabicName}</p>
                  ${item.printDescription ? `
                    <div class="print-description">
                      <span>${item.description}</span>
                      <span lang="ar" dir="rtl">${item.arabicDescription}</span>
                    </div>` : ""}
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

  const renderEditorialNote = (english, arabic) => `
    <aside class="print-note">
      <p>${english}</p>
      <p lang="ar" dir="rtl">${arabic}</p>
    </aside>`;

  const renderFooter = () => `
    <footer>
      <span>Prices shown in Omani Rial</span>
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
      ${renderEditorialNote(data.venue.coffeeStatement, data.venue.arabicCoffeeStatement)}
      <section class="print-menu">
        ${renderColumn(["signature", "black-coffee"])}
        ${renderColumn(["coffee-with-milk"])}
      </section>
      ${renderFooter()}
    </section>
    <section class="sheet">
      ${renderHeader(true)}
      ${renderEditorialNote(data.venue.dessertStatement, data.venue.arabicDessertStatement)}
      <section class="print-menu print-menu-continuation">
        ${renderColumn(["chocolate-and-specials", "desserts"])}
        ${renderColumn(["tea", "juices", "smoothies-and-shakes", "mojitos", "water"])}
      </section>
      ${renderFooter()}
    </section>`;
})();
