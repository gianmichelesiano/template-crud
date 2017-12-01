import { TemplateCrudPage } from './app.po';

describe('template-crud App', () => {
  let page: TemplateCrudPage;

  beforeEach(() => {
    page = new TemplateCrudPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
