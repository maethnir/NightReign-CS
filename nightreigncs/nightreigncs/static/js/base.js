// Accordion behavior
function toggleAccordion(clicked, group) {
  const container = document.getElementById(`${group}-accordion`);
  const items = container.getElementsByClassName('accordion-item');

  for (let item of items) {
    item.classList.remove('active');
  }

  clicked.classList.add('active');
}

// Populate Nightlord info
function selectNightlord(selectElement) {
  const nightlordId = selectElement.value;
  const selectedOption = selectElement.options[selectElement.selectedIndex];

  // Optional: update icon visually (not required here, but available)
  // Load data (in real case, might come from AJAX)
  const data = window.nightlordData[nightlordId];
  if (!data) return;

  // Main Weakness
  const mainWeaknessImg = document.getElementById('main-weakness-icon');
  mainWeaknessImg.src = data.main_weakness.icon_url;
  mainWeaknessImg.alt = data.main_weakness.name;

  // Vulnerabilities
  const vulnList = document.getElementById('vulnerability-list');
  vulnList.innerHTML = ''; // Clear existing

  data.vulnerabilities.forEach(v => {
    const div = document.createElement('div');
    div.className = 'vulnerability-entry';

    const img = document.createElement('img');
    img.src = v.icon_url;
    img.alt = v.name;

    const label = document.createElement('span');
    label.textContent = `${v.name} (${v.percent}%)`;

    div.appendChild(img);
    div.appendChild(label);
    vulnList.appendChild(div);
  });
}

// Optional: preload data (replace with server-side JSON dump if needed)
window.nightlordData = {
  "1": {
    main_weakness: { name: "Fire", icon_url: "/media/Damage/fire.png" },
    vulnerabilities: [
      { name: "Ice", percent: 25, icon_url: "/media/Damage/ice.png" },
      { name: "Lightning", percent: 10, icon_url: "/media/Damage/lightning.png" }
    ]
  },
  // Add more entries keyed by Nightlord ID
};

// Initialize default selection on page load
document.addEventListener('DOMContentLoaded', function () {
  const select = document.getElementById('nightlord-select');
  if (select && select.options.length > 0) {
    selectNightlord(select);
  }
});
