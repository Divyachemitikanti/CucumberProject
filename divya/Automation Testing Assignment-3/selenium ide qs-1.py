{
  "id": "9b384438-8f49-4fb2-b3c0-07b12388222d",
  "version": "2.0",
  "name": "selenium ide",
  "url": "https://demo.opencart.com",
  "tests": [{
    "id": "556d1f7c-e7bc-4bb9-bdfc-1d38423d871a",
    "name": "opencart",
    "commands": [{
      "id": "833b9a53-737d-4f16-b202-9ec8de7a77ad",
      "comment": "",
      "command": "open",
      "target": "/",
      "targets": [],
      "value": ""
    }, {
      "id": "bd3866a9-2f25-4e77-979a-80b7257c574d",
      "comment": "",
      "command": "setWindowSize",
      "target": "1550x830",
      "targets": [],
      "value": ""
    }, {
      "id": "30e5dfed-78d1-405c-a0ad-c1c598ac7a80",
      "comment": "",
      "command": "click",
      "target": "linkText=Desktops",
      "targets": [
        ["linkText=Desktops", "linkText"],
        ["css=.show:nth-child(1)", "css:finder"],
        ["xpath=//a[contains(text(),'Desktops')]", "xpath:link"],
        ["xpath=//div[@id='narbar-menu']/ul/li/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'https://demo.opencart.com/en-gb/catalog/desktops')]", "xpath:href"],
        ["xpath=//nav/div[2]/ul/li/a", "xpath:position"],
        ["xpath=//a[contains(.,'Desktops')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "c48f1895-eca6-4e6a-a61c-94388e5ad978",
      "comment": "",
      "command": "click",
      "target": "linkText=Mac (1)",
      "targets": [
        ["linkText=Mac (1)", "linkText"],
        ["css=.show li:nth-child(2) > .nav-link", "css:finder"],
        ["xpath=//a[contains(text(),'Mac (1)')]", "xpath:link"],
        ["xpath=//div[@id='narbar-menu']/ul/li/div/div/ul/li[2]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'https://demo.opencart.com/en-gb/catalog/desktops/mac')]", "xpath:href"],
        ["xpath=//div/div/ul/li[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Mac (1)')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "f45a32da-ab7a-479a-87cf-547fa419a08d",
      "comment": "",
      "command": "mouseDownAt",
      "target": "id=input-sort",
      "targets": [
        ["id=input-sort", "id"],
        ["css=#input-sort", "css:finder"],
        ["xpath=//select[@id='input-sort']", "xpath:attributes"],
        ["xpath=//div[@id='display-control']/div[3]/div/select", "xpath:idRelative"],
        ["xpath=//select", "xpath:position"]
      ],
      "value": "-929.7333374023438,-402"
    }, {
      "id": "09036f97-fd60-451c-ab59-5ae25c31ff76",
      "comment": "",
      "command": "mouseMoveAt",
      "target": "id=input-sort",
      "targets": [
        ["id=input-sort", "id"],
        ["css=#input-sort", "css:finder"],
        ["xpath=//select[@id='input-sort']", "xpath:attributes"],
        ["xpath=//div[@id='display-control']/div[3]/div/select", "xpath:idRelative"],
        ["xpath=//select", "xpath:position"]
      ],
      "value": "-929.7333374023438,-402"
    }, {
      "id": "6ea740a7-77b2-4aa9-a121-9aad444f9b7d",
      "comment": "",
      "command": "mouseUpAt",
      "target": "id=input-sort",
      "targets": [
        ["id=input-sort", "id"],
        ["css=#input-sort", "css:finder"],
        ["xpath=//select[@id='input-sort']", "xpath:attributes"],
        ["xpath=//div[@id='display-control']/div[3]/div/select", "xpath:idRelative"],
        ["xpath=//select", "xpath:position"]
      ],
      "value": "-929.7333374023438,-402"
    }, {
      "id": "a2ea3b2d-d3fb-4c6d-afea-e7a46326cd5e",
      "comment": "",
      "command": "click",
      "target": "id=input-sort",
      "targets": [
        ["id=input-sort", "id"],
        ["css=#input-sort", "css:finder"],
        ["xpath=//select[@id='input-sort']", "xpath:attributes"],
        ["xpath=//div[@id='display-control']/div[3]/div/select", "xpath:idRelative"],
        ["xpath=//select", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b27fe793-0e1e-4a61-9d81-231333ee659b",
      "comment": "",
      "command": "select",
      "target": "id=input-sort",
      "targets": [],
      "value": "label=Name (A - Z)"
    }, {
      "id": "8a88eaa3-8e09-41ad-91f2-96ac40e503d1",
      "comment": "",
      "command": "click",
      "target": "css=#input-sort > option:nth-child(2)",
      "targets": [
        ["css=#input-sort > option:nth-child(2)", "css:finder"],
        ["xpath=//option[@value='https://demo.opencart.com/en-gb/catalog/desktops/mac?sort=pd.name&order=ASC']", "xpath:attributes"],
        ["xpath=//select[@id='input-sort']/option[2]", "xpath:idRelative"],
        ["xpath=//option[2]", "xpath:position"],
        ["xpath=//option[contains(.,'Name (A - Z)')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "1cd463bd-1f3e-49c5-bfcf-8737da7f5a0b",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0,288.79998779296875)",
      "targets": [],
      "value": ""
    }, {
      "id": "99bb77cf-4464-4a77-aeb4-6e8c46c66240",
      "comment": "",
      "command": "click",
      "target": "css=.button-group > button:nth-child(1)",
      "targets": [
        ["css=.button-group > button:nth-child(1)", "css:finder"],
        ["xpath=(//button[@type='submit'])[2]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button", "xpath:idRelative"],
        ["xpath=//form/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "5629f5c0-7997-4338-859c-4f978ef403c4",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.button-group > button:nth-child(2)",
      "targets": [
        ["css=.button-group > button:nth-child(2)", "css:finder"],
        ["xpath=(//button[@type='submit'])[3]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button[2]", "xpath:idRelative"],
        ["xpath=//form/div/button[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7215e810-890b-4e61-b661-cbcd9c1e7633",
      "comment": "",
      "command": "mouseOut",
      "target": "css=.button-group > button:nth-child(2)",
      "targets": [
        ["css=.button-group > button:nth-child(2)", "css:finder"],
        ["xpath=(//button[@type='submit'])[3]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button[2]", "xpath:idRelative"],
        ["xpath=//form/div/button[2]", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "0229cdff-f3fb-4b30-8970-b8c24a729114",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["556d1f7c-e7bc-4bb9-bdfc-1d38423d871a"]
  }],
  "urls": ["https://demo.opencart.com/"],
  "plugins": []
}