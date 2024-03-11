from selene import browser, be, have


#def test():
    browser.open('https://zkillboard.com')
    browser.element('[id="searchbox"]').should(be.blank).type('Brain Cancer').press_enter()
    browser.element('.name').should(have.text('Brain Cancer'))
