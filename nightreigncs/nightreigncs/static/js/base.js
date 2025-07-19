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

function selectExpedition(selectElement) {
  const expeditionId = selectElement.value;
  const nightlords = window.nightlordData[expeditionId];
  const expedition = window.expeditionData[expeditionId];
  const selectorSection = document.getElementById("nightlord-selection");
  const infoSection = document.getElementById("nightlord-info");

  // Remove previously added expedition icons only
  const existingIcons = selectorSection.querySelectorAll('.expedition-icon');
  existingIcons.forEach(icon => icon.remove());

  // Add new expedition icon
  const expeditionIcon = document.createElement("img");
  expeditionIcon.src = expedition.icon_url;
  expeditionIcon.alt = expedition.name;
  expeditionIcon.title = expedition.name;
  expeditionIcon.classList.add("expedition-icon"); // tag it
  selectorSection.appendChild(expeditionIcon);

  infoSection.innerHTML = '';

  if (!nightlords || nightlords.length === 0) {
    infoSection.innerHTML = '<p>No Nightlords found for this expedition.</p>';
    return;
  }

  nightlords.forEach(nl => {
    const nlDiv = document.createElement("div");
    nlDiv.classList.add("nightlord-entry");

    const title = document.createElement("h3");
    title.textContent = nl.name;

    const vulnList = document.createElement("div");
    vulnList.classList.add("other-vulnerabilities")

    nl.vulnerabilities.forEach(vuln => {
      const vulnDiv = document.createElement("div");
      vulnDiv.classList.add("vulnerability-entry");

      const vulnImg = document.createElement("img");
      if(vuln.name == nl.main_weakness.name){
        vulnDiv.classList.add("main-weakness")
      }
      vulnImg.src = vuln.icon_url;
      vulnImg.alt = vuln.name;
      vulnImg.title = vuln.name;
      
      const vulnText = document.createElement("span");
      vulnText.textContent = vuln.is_condition ? vuln.value==0 ? `Immune`: ` ${vuln.value}`:` ${vuln.value}%`;

      vulnDiv.appendChild(vulnImg);
      vulnDiv.appendChild(vulnText);
      vulnList.appendChild(vulnDiv);
    });

    nlDiv.appendChild(title);
    nlDiv.appendChild(vulnList);

    infoSection.appendChild(nlDiv);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const select = document.getElementById("expedition-select");
  if (select && select.value) {
    selectExpedition(select);
  }
});

