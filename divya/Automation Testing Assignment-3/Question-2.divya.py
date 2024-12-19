{
  "id": "9f45e180-0edd-4fd3-aecd-4a7b5bcaf558",
  "version": "2.0",
  "name": "opencart",
  "url": "https://demo.opencart.com/",
  "tests": [{
    "id": "ff170f3a-3f2c-4045-9d6b-7fa9851bd5e8",
    "name": "opentestcase",
    "commands": [{
      "id": "e632d8c8-0bcb-4f07-8f7f-3b22c71cc9d7",
      "comment": "",
      "command": "open",
      "target": "/",
      "targets": [],
      "value": ""
    }, {
      "id": "eac1e16f-34fe-4f7c-bd2b-b503128db79e",
      "comment": "",
      "command": "setWindowSize",
      "target": "1536x703",
      "targets": [],
      "value": ""
    }, {
      "id": "406361be-f584-4139-9c66-d6170453e49a",
      "comment": "",
      "command": "click",
      "target": "css=#logo .img-fluid",
      "targets": [
        ["css=#logo .img-fluid", "css:finder"],
        ["xpath=//img[@alt='Your Store']", "xpath:img"],
        ["xpath=//div[@id='logo']/a/img", "xpath:idRelative"],
        ["xpath=//img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "0ee4474c-37c2-4158-a2c8-0a4e03352d0d",
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
      "id": "69fc64bd-f3ad-45da-9f4f-68bb4a1cf5e4",
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
      "id": "6a73f0df-aa0d-46bc-98e2-ed70f0d95657",
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
      "value": "-924.13330078125,-402"
    }, {
      "id": "9e3ef323-ad28-4f94-86a7-040d1a60f9d4",
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
      "value": "-924.13330078125,-402"
    }, {
      "id": "4bcf81cb-b591-497b-925b-c4674c6a498c",
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
      "value": "-924.13330078125,-402"
    }, {
      "id": "20edcd54-cbf2-45aa-a5d4-0d3b9030adb8",
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
      "id": "6426aa05-038c-42c1-8c7f-22d057ff16c7",
      "comment": "",
      "command": "select",
      "target": "id=input-sort",
      "targets": [],
      "value": "label=Name (A - Z)"
    }, {
      "id": "a478aa2f-55fa-4626-8677-59413bae17e4",
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
      "id": "4f4b3156-96f0-42df-a392-60d58f2a737a",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.button-group > button:nth-child(1)",
      "targets": [
        ["css=.button-group > button:nth-child(1)", "css:finder"],
        ["xpath=(//button[@type='submit'])[2]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button", "xpath:idRelative"],
        ["xpath=//form/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "898e18c5-f4b0-455a-977f-533dad25fb03",
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
      "id": "885289df-8427-45cd-bc7a-3923f56962b8",
      "comment": "",
      "command": "mouseOut",
      "target": "css=.button-group > button:nth-child(1)",
      "targets": [
        ["css=.button-group > button:nth-child(1)", "css:finder"],
        ["xpath=(//button[@type='submit'])[2]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button", "xpath:idRelative"],
        ["xpath=//form/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "f04bd72b-ced5-424f-9f85-ed22e120265f",
      "comment": "",
      "command": "click",
      "target": "name=search",
      "targets": [
        ["name=search", "name"],
        ["css=.form-control", "css:finder"],
        ["xpath=//input[@name='search']", "xpath:attributes"],
        ["xpath=//div[@id='search']/input", "xpath:idRelative"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "25467522-bd27-4a52-9883-24baa64e7289",
      "comment": "",
      "command": "type",
      "target": "name=search",
      "targets": [
        ["name=search", "name"],
        ["css=.form-control", "css:finder"],
        ["xpath=//input[@name='search']", "xpath:attributes"],
        ["xpath=//div[@id='search']/input", "xpath:idRelative"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": "mobile"
    }, {
      "id": "0a9f67e1-82f5-4ac5-9120-7af1fd39043f",
      "comment": "",
      "command": "click",
      "target": "css=.btn-lg:nth-child(2)",
      "targets": [
        ["css=.btn-lg:nth-child(2)", "css:finder"],
        ["xpath=//button[@type='button']", "xpath:attributes"],
        ["xpath=//div[@id='search']/button", "xpath:idRelative"],
        ["xpath=//button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4278043a-ab89-4981-babe-6d82871bab1d",
      "comment": "",
      "command": "click",
      "target": "id=input-description",
      "targets": [
        ["id=input-description", "id"],
        ["name=description", "name"],
        ["css=#input-description", "css:finder"],
        ["xpath=//input[@id='input-description']", "xpath:attributes"],
        ["xpath=//div[@id='content']/div[2]/div/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "697ef085-5d25-46d5-bd79-aea7a6d54a3b",
      "comment": "",
      "command": "click",
      "target": "id=button-search",
      "targets": [
        ["id=button-search", "id"],
        ["css=#button-search", "css:finder"],
        ["xpath=//button[@id='button-search']", "xpath:attributes"],
        ["xpath=//div[@id='content']/div[3]/div/button", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/div[3]/div/button", "xpath:position"],
        ["xpath=//button[contains(.,'Search')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "ca4a1ce9-930f-4364-ae4d-4670c0687ab2",
      "comment": "",
      "command": "click",
      "target": "id=button-search",
      "targets": [
        ["id=button-search", "id"],
        ["css=#button-search", "css:finder"],
        ["xpath=//button[@id='button-search']", "xpath:attributes"],
        ["xpath=//div[@id='content']/div[3]/div/button", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/div[3]/div/button", "xpath:position"],
        ["xpath=//button[contains(.,'Search')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "ee3471e5-5384-488d-afe2-f5930c237339",
    "name": "test-2",
    "commands": [{
      "id": "c57dd346-fee2-4061-b165-d7d55a609ebe",
      "comment": "",
      "command": "open",
      "target": "https://demo.opencart.com/",
      "targets": [],
      "value": ""
    }, {
      "id": "8d87bf64-0c2c-48ef-90ec-0aac3c5a55a0",
      "comment": "",
      "command": "setWindowSize",
      "target": "1536x703",
      "targets": [],
      "value": ""
    }, {
      "id": "27cd6d04-b0ea-471e-8641-cfad6a7d860b",
      "comment": "",
      "command": "click",
      "target": "name=search",
      "targets": [
        ["name=search", "name"],
        ["css=.form-control", "css:finder"],
        ["xpath=//input[@name='search']", "xpath:attributes"],
        ["xpath=//div[@id='search']/input", "xpath:idRelative"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "08acf666-140b-4d39-8bcb-0a2d74a22e64",
      "comment": "",
      "command": "type",
      "target": "name=search",
      "targets": [
        ["name=search", "name"],
        ["css=.form-control", "css:finder"],
        ["xpath=//input[@name='search']", "xpath:attributes"],
        ["xpath=//div[@id='search']/input", "xpath:idRelative"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": "monitors"
    }, {
      "id": "36214a74-a961-4166-b84f-24aea38f9ba0",
      "comment": "",
      "command": "click",
      "target": "css=.btn-light",
      "targets": [
        ["css=.btn-light", "css:finder"],
        ["xpath=//button[@type='button']", "xpath:attributes"],
        ["xpath=//div[@id='search']/button", "xpath:idRelative"],
        ["xpath=//button", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "f1f1bd6c-78e9-48f1-a538-b5bd76aead89",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["ff170f3a-3f2c-4045-9d6b-7fa9851bd5e8"]
  }],
  "urls": ["https://demo.opencart.com/"],
  "plugins": []
}









{
  "id": "9f45e180-0edd-4fd3-aecd-4a7b5bcaf558",
  "version": "2.0",
  "name": "opencart",
  "url": "https://demo.opencart.com/",
  "tests": [{
    "id": "ff170f3a-3f2c-4045-9d6b-7fa9851bd5e8",
    "name": "opentestcase",
    "commands": [{
      "id": "e632d8c8-0bcb-4f07-8f7f-3b22c71cc9d7",
      "comment": "",
      "command": "open",
      "target": "/",
      "targets": [],
      "value": ""
    }, {
      "id": "eac1e16f-34fe-4f7c-bd2b-b503128db79e",
      "comment": "",
      "command": "setWindowSize",
      "target": "1536x703",
      "targets": [],
      "value": ""
    }, {
      "id": "406361be-f584-4139-9c66-d6170453e49a",
      "comment": "",
      "command": "click",
      "target": "css=#logo .img-fluid",
      "targets": [
        ["css=#logo .img-fluid", "css:finder"],
        ["xpath=//img[@alt='Your Store']", "xpath:img"],
        ["xpath=//div[@id='logo']/a/img", "xpath:idRelative"],
        ["xpath=//img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "0ee4474c-37c2-4158-a2c8-0a4e03352d0d",
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
      "id": "69fc64bd-f3ad-45da-9f4f-68bb4a1cf5e4",
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
      "id": "6a73f0df-aa0d-46bc-98e2-ed70f0d95657",
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
      "value": "-924.13330078125,-402"
    }, {
      "id": "9e3ef323-ad28-4f94-86a7-040d1a60f9d4",
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
      "value": "-924.13330078125,-402"
    }, {
      "id": "4bcf81cb-b591-497b-925b-c4674c6a498c",
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
      "value": "-924.13330078125,-402"
    }, {
      "id": "20edcd54-cbf2-45aa-a5d4-0d3b9030adb8",
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
      "id": "6426aa05-038c-42c1-8c7f-22d057ff16c7",
      "comment": "",
      "command": "select",
      "target": "id=input-sort",
      "targets": [],
      "value": "label=Name (A - Z)"
    }, {
      "id": "a478aa2f-55fa-4626-8677-59413bae17e4",
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
      "id": "4f4b3156-96f0-42df-a392-60d58f2a737a",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.button-group > button:nth-child(1)",
      "targets": [
        ["css=.button-group > button:nth-child(1)", "css:finder"],
        ["xpath=(//button[@type='submit'])[2]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button", "xpath:idRelative"],
        ["xpath=//form/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "898e18c5-f4b0-455a-977f-533dad25fb03",
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
      "id": "885289df-8427-45cd-bc7a-3923f56962b8",
      "comment": "",
      "command": "mouseOut",
      "target": "css=.button-group > button:nth-child(1)",
      "targets": [
        ["css=.button-group > button:nth-child(1)", "css:finder"],
        ["xpath=(//button[@type='submit'])[2]", "xpath:attributes"],
        ["xpath=//div[@id='product-list']/div/div/div[2]/form/div/button", "xpath:idRelative"],
        ["xpath=//form/div/button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "f04bd72b-ced5-424f-9f85-ed22e120265f",
      "comment": "",
      "command": "click",
      "target": "name=search",
      "targets": [
        ["name=search", "name"],
        ["css=.form-control", "css:finder"],
        ["xpath=//input[@name='search']", "xpath:attributes"],
        ["xpath=//div[@id='search']/input", "xpath:idRelative"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "25467522-bd27-4a52-9883-24baa64e7289",
      "comment": "",
      "command": "type",
      "target": "name=search",
      "targets": [
        ["name=search", "name"],
        ["css=.form-control", "css:finder"],
        ["xpath=//input[@name='search']", "xpath:attributes"],
        ["xpath=//div[@id='search']/input", "xpath:idRelative"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": "mobile"
    }, {
      "id": "0a9f67e1-82f5-4ac5-9120-7af1fd39043f",
      "comment": "",
      "command": "click",
      "target": "css=.btn-lg:nth-child(2)",
      "targets": [
        ["css=.btn-lg:nth-child(2)", "css:finder"],
        ["xpath=//button[@type='button']", "xpath:attributes"],
        ["xpath=//div[@id='search']/button", "xpath:idRelative"],
        ["xpath=//button", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4278043a-ab89-4981-babe-6d82871bab1d",
      "comment": "",
      "command": "click",
      "target": "id=input-description",
      "targets": [
        ["id=input-description", "id"],
        ["name=description", "name"],
        ["css=#input-description", "css:finder"],
        ["xpath=//input[@id='input-description']", "xpath:attributes"],
        ["xpath=//div[@id='content']/div[2]/div/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "697ef085-5d25-46d5-bd79-aea7a6d54a3b",
      "comment": "",
      "command": "click",
      "target": "id=button-search",
      "targets": [
        ["id=button-search", "id"],
        ["css=#button-search", "css:finder"],
        ["xpath=//button[@id='button-search']", "xpath:attributes"],
        ["xpath=//div[@id='content']/div[3]/div/button", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/div[3]/div/button", "xpath:position"],
        ["xpath=//button[contains(.,'Search')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "ca4a1ce9-930f-4364-ae4d-4670c0687ab2",
      "comment": "",
      "command": "click",
      "target": "id=button-search",
      "targets": [
        ["id=button-search", "id"],
        ["css=#button-search", "css:finder"],
        ["xpath=//button[@id='button-search']", "xpath:attributes"],
        ["xpath=//div[@id='content']/div[3]/div/button", "xpath:idRelative"],
        ["xpath=//div[2]/div/div/div[3]/div/button", "xpath:position"],
        ["xpath=//button[contains(.,'Search')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "ee3471e5-5384-488d-afe2-f5930c237339",
    "name": "test-2",
    "commands": [{
      "id": "c57dd346-fee2-4061-b165-d7d55a609ebe",
      "comment": "",
      "command": "open",
      "target": "https://demo.opencart.com/",
      "targets": [],
      "value": ""
    }, {
      "id": "8d87bf64-0c2c-48ef-90ec-0aac3c5a55a0",
      "comment": "",
      "command": "setWindowSize",
      "target": "1536x703",
      "targets": [],
      "value": ""
    }, {
      "id": "27cd6d04-b0ea-471e-8641-cfad6a7d860b",
      "comment": "",
      "command": "click",
      "target": "name=search",
      "targets": [
        ["name=search", "name"],
        ["css=.form-control", "css:finder"],
        ["xpath=//input[@name='search']", "xpath:attributes"],
        ["xpath=//div[@id='search']/input", "xpath:idRelative"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "08acf666-140b-4d39-8bcb-0a2d74a22e64",
      "comment": "",
      "command": "type",
      "target": "name=search",
      "targets": [
        ["name=search", "name"],
        ["css=.form-control", "css:finder"],
        ["xpath=//input[@name='search']", "xpath:attributes"],
        ["xpath=//div[@id='search']/input", "xpath:idRelative"],
        ["xpath=//div/input", "xpath:position"]
      ],
      "value": "monitors"
    }, {
      "id": "36214a74-a961-4166-b84f-24aea38f9ba0",
      "comment": "",
      "command": "click",
      "target": "css=.btn-light",
      "targets": [
        ["css=.btn-light", "css:finder"],
        ["xpath=//button[@type='button']", "xpath:attributes"],
        ["xpath=//div[@id='search']/button", "xpath:idRelative"],
        ["xpath=//button", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "f1f1bd6c-78e9-48f1-a538-b5bd76aead89",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["ff170f3a-3f2c-4045-9d6b-7fa9851bd5e8"]
  }],
  "urls": ["https://demo.opencart.com/"],
  "plugins": []
}