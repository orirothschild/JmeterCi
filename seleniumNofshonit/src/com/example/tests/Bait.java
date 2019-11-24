package com.example.tests;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class Bait {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
    driver = new FirefoxDriver();
    baseUrl = "https://www.katalon.com/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testUntitledTestCase() throws Exception {
    driver.get("https://pp-nofshonitnewwebclient.dts.co.il/");
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='טוען תוצאות...'])[1]/following::div[5]")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התחברות / הרשמה'])[1]/following::button[1]")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='המשך עם גוגל'])[1]/following::button[1]")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התחברות באמצעות מייל'])[1]/following::input[1]")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התחברות באמצעות מייל'])[1]/following::input[1]")).clear();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התחברות באמצעות מייל'])[1]/following::input[1]")).sendKeys("shabtaiuser_225529555@dts-4u.com");
    driver.findElement(By.name("password")).click();
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("Hello_0735");
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התחברות באמצעות מייל'])[1]/following::button[1]")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='×'])[1]/following::button[1]")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התחברות / הרשמה'])[1]/following::button[1]")).click();
    driver.findElement(By.xpath("(//input[@name='email'])[2]")).click();
    driver.findElement(By.xpath("(//input[@name='email'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='email'])[2]")).sendKeys("shabtaiuser_225529555@dts-4u.com");
    driver.findElement(By.name("password")).click();
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("Hello_0735");
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התחברות באמצעות מייל'])[1]/following::button[1]")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התחברות בוצעה בהצלחה'])[1]/following::button[1]")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התנתק'])[1]/following::div[9]")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התנתק'])[1]/following::div[9]")).click();
    driver.findElement(By.xpath("//div[@id='__next']/div/div[2]/div[2]/div/div/div/div/div/div[3]/i")).click();
    driver.findElement(By.linkText("התנתק")).click();
    driver.findElement(By.xpath("//div[@id='__next']/div/div[2]/div[2]/div/div/div/div/div/div[3]/i")).click();
    driver.findElement(By.linkText("התנתק")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התחברות / הרשמה'])[1]/following::button[1]")).click();
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='המשך עם גוגל'])[1]/following::button[1]")).click();
    driver.findElement(By.name("password")).click();
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("Hello_0735");
    driver.findElement(By.xpath("(//input[@name='email'])[2]")).click();
    driver.findElement(By.xpath("(//input[@name='email'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='email'])[2]")).sendKeys("shabtaiuser_225529555@dts-4u.com");
    driver.findElement(By.xpath("(.//*[normalize-space(text()) and normalize-space(.)='התחברות באמצעות מייל'])[1]/following::button[1]")).click();
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
