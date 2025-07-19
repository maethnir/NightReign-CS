function toggleAccordion(element, group) {
  const items = document.querySelectorAll(`.accordion-vertical[id$="-accordion"] .accordion-item`);
  items.forEach(item => {
    if (item === element && !item.classList.contains('active')) {
      item.classList.add('active');
    } else {
      item.classList.remove('active');
    }
  });
}

function selectNightlord(selectElement) {
  const selectedId = selectElement.value;
  const nightlord = window.nightlordData[selectedId];

  if (nightlord) {
    const mainWeaknessIcon = document.getElementById('main-weakness-icon');
    mainWeaknessIcon.src = nightlord.main_weakness.icon_url;
    mainWeaknessIcon.alt = nightlord.main_weakness.name;

    const vulnerabilityList = document.getElementById('vulnerability-list');
    vulnerabilityList.innerHTML = '';

    nightlord.vulnerabilities.forEach(vuln => {
      const vulnDiv = document.createElement('div');
      const vulnImg = document.createElement('img');
      vulnImg.src = vuln.icon_url;
      vulnImg.alt = vuln.name;
      const vulnPercent = document.createElement('p');
      vulnPercent.textContent = `${vuln.percent}%`;

      vulnDiv.appendChild(vulnImg);
      vulnDiv.appendChild(vulnPercent);
      vulnerabilityList.appendChild(vulnDiv);
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const firstNightlord = document.querySelector('#nightlord-select option');
  if (firstNightlord) {
    selectNightlord(document.getElementById('nightlord-select'));
  }
});
