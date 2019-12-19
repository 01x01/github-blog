---
title: Java前端自动化测试 
date: 2019-12-18
tags: testng,selenium,allure,jenkins
category: 测试
---
# 概述
基于 testng + allure + selenium + jenkins 
# POM.xml
第一步首先构建 POM.xml 文件，分为以下几步
1. 属性定义，这一步可以定义一些依赖的版本，还有配置等等，当然也可以为空，最后在 mvn 的时候传入参数
```xml
<properties>
    <aspectj.version>1.8.10</aspectj.version>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>
```
2. 添加依赖
示例
```xml
<dependency>
     <groupId>io.qameta.allure</groupId>
     <artifactId>allure-testng</artifactId>
     <version>${allure-testng.verion}</version>
</dependency>
...
```
3. build 插件
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
            </configuration>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>2.20</version>
            <configuration>
                <suiteXmlFiles>
                    <suiteXmlFile>TestNG.xml</suiteXmlFile>
                </suiteXmlFiles>
                <argLine>
                    -javaagent:"${settings.localRepository}/org/aspectj/aspectjweaver/${aspectj.version}/aspectjweaver-${aspectj.version}.jar"
                </argLine>
            </configuration>
            <dependencies>
                <dependency>
                    <groupId>org.aspectj</groupId>
                    <artifactId>aspectjweaver</artifactId>
                    <version>${aspectj.version}</version>
                </dependency>
            </dependencies>
        </plugin>
    </plugins>
</build>
```
最后，我们可以看到一个完整的 pom.xml 文件
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.ehi.Sample</groupId>
    <artifactId>sample</artifactId>
    <version>1.0-SNAPSHOT</version>
    <properties>
        <allure.version>2.13.1</allure.version>
        <java.version>1.8</java.version>
        <aspectj.version>1.8.10</aspectj.version>
        <selenium.version>4.0.0-alpha-3</selenium.version>
        <log4j.version>1.2.17</log4j.version>
        <testng.version>6.14.3</testng.version>
        <hamcrest.version>1.3</hamcrest.version>
        <slf4j.version>1.7.30</slf4j.version>
        <testng.version>6.14.3</testng.version>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java -->
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>${selenium.version}</version>
        </dependency>

        <dependency>
            <groupId>log4j</groupId>
            <artifactId>log4j</artifactId>
            <version>${log4j.version}</version>
        </dependency>
        <!-- https://github.com/allure-examples/allure-testng-example/blob/master/pom.xml -->
        <dependency>
            <groupId>org.testng</groupId>
            <artifactId>testng</artifactId>
            <version>${testng.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>io.qameta.allure</groupId>
            <artifactId>allure-testng</artifactId>
            <version>${allure.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>ru.yandex.qatools.allure</groupId>
            <artifactId>allure-maven-plugin</artifactId>
            <version>2.6</version>
        </dependency>
        <!-- https://mvnrepository.com/artifact/commons-io/commons-io -->
        <dependency>
            <groupId>commons-io</groupId>
            <artifactId>commons-io</artifactId>
            <version>2.5</version>
        </dependency>

        <dependency>
            <groupId>org.hamcrest</groupId>
            <artifactId>hamcrest-all</artifactId>
            <version>${hamcrest.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-simple</artifactId>
            <version>${slf4j.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.testng</groupId>
            <artifactId>testng</artifactId>
            <version>7.0.0</version>
            <scope>compile</scope>
        </dependency>
        <dependency>
            <groupId>io.qameta.allure</groupId>
            <artifactId>allure-java-commons</artifactId>
            <version>2.13.1</version>
            <scope>compile</scope>
        </dependency>


    </dependencies>
    <!-- https://github.com/allure-examples/allure-testng-example/blob/master/pom.xml -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>2.22.2</version>
                <configuration>
                    <suiteXmlFiles>
                        <suiteXmlFile>testng.xml</suiteXmlFile>
                    </suiteXmlFiles>
                    <argLine>
                        -javaagent:"${settings.localRepository}/org/aspectj/aspectjweaver/${aspectj.version}/aspectjweaver-${aspectj.version}.jar"
                    </argLine>
                </configuration>
                <dependencies>
                    <dependency>
                        <groupId>org.aspectj</groupId>
                        <artifactId>aspectjweaver</artifactId>
                        <version>${aspectj.version}</version>
                    </dependency>
                    <dependency>
                        <groupId>org.apache.maven.plugins</groupId>
                        <artifactId>maven-resources-plugin</artifactId>
                        <version>3.1.0</version>
                    </dependency>
                </dependencies>
            </plugin>
            <plugin>
                <artifactId>maven-resources-plugin</artifactId>
                <version>3.1.0</version>
                <configuration>
                    <encoding>UTF-8</encoding>
                    <overwrite>true</overwrite>
                </configuration>
                <executions>
                    <execution>
                        <id>copy-resources</id>
                        <phase>validate</phase>
                        <goals>
                            <goal>copy-resources</goal>
                        </goals>
                        <configuration>
                            <outputDirectory>${basedir}/allure-results/history</outputDirectory>
                            <resources>
                                <resource>
                                    <directory>${basedir}/allure-report/history</directory>
                                    <filtering>true</filtering>
                                </resource>
                            </resources>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>io.qameta.allure</groupId>
                <artifactId>allure-maven</artifactId>
                <version>2.10.0</version>
                <configuration>
                    <reportDirectory>${basedir}/allure-report</reportDirectory>
                    <resultsDirectory>${basedir}/allure-results</resultsDirectory>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
# 编写前端自动化测试用例
这里我们以一个登陆功能为例子进行测试，在写前端自动化脚本的时候，我们大多以page object 的方式来做，这里就以一个简单的登陆功能为例子。首先写 page

```Java
// BasePage.java
package com.ehi.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class BasePage {
    public WebDriver driver;
    public WebDriverWait wait;

    public BasePage(WebDriver driver){
        this.driver = driver;
        wait = new WebDriverWait(driver,20);
    }

    public void click(By element){
        driver.findElement(element).click();
    }
    public void send(By element, String text){
        driver.findElement(element).sendKeys(text);
    }
    public String getText(By element){
        return driver.findElement(element).getText();
    }
    public void waitVisibility(By by){
        wait.until(ExpectedConditions.visibilityOfElementLocated(by));
    }
}


// HomePage.java
package com.ehi.pages;

import io.qameta.allure.Step;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class HomePage extends BasePage{
    private String baseURL = "https://www.qa.xxx.com";
    private By signInButton = By.id("sign-in-button");

    public HomePage(WebDriver driver) {
        super(driver);
    }
    @Step("Open HomePage")
    public HomePage goToHomePage(){
        driver.get(baseURL);
        return this;
    }
    @Step("Go to Login Page")
    public LoginPage goToLoginPage(){
        click(signInButton);
        return new LoginPage(driver);
    }
}

//LoginPage.java
package com.ehi.pages;

import io.qameta.allure.Step;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;

public class LoginPage extends BasePage{
    public LoginPage(WebDriver driver) {
        super(driver);
    }
    /**Web Elements*/
    By userNameId = By.id("email");
    By passwordId = By.id("password");
    By loginButtonId = By.id("loginButton");
    By errorMessageUsernameXpath = By.xpath("//*[@id=\"loginForm\"]/div[1]/div/div");
    By errorMessagePasswordXpath = By.xpath("//*[@id=\"loginForm\"]/div[2]/div/div ");

    /**Page Methods*/
    @Step("Login Step with username: {0}, password: {1}, for method: {method} step...")
    public LoginPage loginToN11(String username, String password) {
        send(userNameId, username);
        send(passwordId, password);
        click(loginButtonId);
        return this;
    }

    //Verify Username Condition
    @Step("Verify username: {0} step...")
    public LoginPage verifyLoginUserName(String expectedText) {
        waitVisibility(errorMessageUsernameXpath);
        Assert.assertEquals(getText(errorMessageUsernameXpath), expectedText);
        return this;
    }

    //Verify Password Condition
    @Step("Verify verifyLoginPassword: {0} step...")
    public LoginPage verifyLoginPassword(String expectedText) {
        waitVisibility(errorMessagePasswordXpath);
        Assert.assertEquals(getText(errorMessagePasswordXpath), expectedText);
        return this;
    }
}
```

page 完成以后，我们就可以在 testcase 中通过组装 page 和操作来实现

```Java
// BaseTestCase
package com.ehi.testcases;

import com.ehi.pages.HomePage;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;

public class BaseTestCase {
    public WebDriver driver;
    public HomePage homePage;

    public WebDriver getDriver() {
        return driver;
    }

    @BeforeClass
    public void classLevelSetup() {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\johnw\\Documents\\checkmarx\\chromedriver.exe");
        driver = new ChromeDriver();
    }

    @BeforeMethod
    public void methodLevelSetup() {
        homePage = new HomePage(driver);
    }

    @AfterClass
    public void teardown() {
        driver.quit();
    }
}

// LoginTestCase
package com.ehi.testcases;

import io.qameta.allure.Severity;
import io.qameta.allure.SeverityLevel;
import io.qameta.allure.Story;
import org.testng.annotations.Test;


public class LoginTestCase extends BaseTestCase{
    private String userName = "test@test.com";
    private String passWord = "qwe123";
    private String verifyText = "We're sorry, the email address or password you entered is incorrect. Please try again.";
    @Test(priority = 0,description = "Invalid username and password")
    @Severity(SeverityLevel.BLOCKER)
    @Story("Invalid username and password login test.")
    public void invalidLoginTest(){
        homePage.goToHomePage().goToLoginPage().login(userName,passWord).verifyLoginPassword(verifyText);
    }
}

```
# 配置 Listener 和 Retry
配置 Listener，主要作用是在测试用例的执行过程中实现一些功能，比如失败的时候截图，完成以后发送邮件等操作
```java
package com.ehi.Listeners;

import com.ehi.testcases.BaseTestCase;
import com.ehi.utils.ScreenshotRobot;
import io.qameta.allure.Attachment;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;

import java.io.File;
import java.io.IOException;

public class TestListener extends BaseTestCase implements ITestListener {
    @Override
    public void onStart(ITestContext context) {
        context.setAttribute("WebDriver", this.driver);
    }
    // 截图操作
    @Attachment(value = "Page Screenshot",type = "image/png")
    public void saveScreenshotPNG(WebDriver driver,String name) {
        try {
            FileUtils.copyFile(((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE), new File("image/"+name+".png"));
        }catch (IOException e){
            e.printStackTrace();
        }
    }
    @Override
    public void onTestStart(ITestResult result) {

    }

    @Override
    public void onTestFailedButWithinSuccessPercentage(ITestResult result) {

    }

    @Override
    public void onTestFailedWithTimeout(ITestResult result) {

    }

    @Override
    public void onTestSkipped(ITestResult result) {

    }
    private static String getTestMethodName(ITestResult iTestResult) {
        return iTestResult.getMethod().getConstructorOrMethod().getName();
    }
    // 失败时进行截图
    @Override
    public void onTestFailure(ITestResult result) {
        System.out.println("I am in onTestFailure method " +  getTestMethodName(result) + " failed");

        //Get driver from BaseTest and assign to local webdriver variable.
        Object testClass = result.getInstance();
        WebDriver driver = ((BaseTestCase) testClass).getDriver();

        //Allure ScreenShotRobot
        System.out.println(driver);
        System.out.println("Screenshot captured for test case:" + getTestMethodName(result));
        saveScreenshotPNG(driver,getTestMethodName(result));
    }

    @Override
    public void onTestSuccess(ITestResult result) {

    }

    @Override
    public void onFinish(ITestContext context) {
        // 发送邮件或者其他操作
    }
}

```

我们在执行测试用例的时候经常会出现用例执行失败的例子，这个时候就需要设置重试的次数，其 retry 的代码如下：
```java
//Retry.java
package com.ehi.utils.Listeners;

import org.testng.IRetryAnalyzer;
import org.testng.ITestResult;

public class Retry implements IRetryAnalyzer {
    private int count = 0;
    private static int maxTry = 3;
    @Override
    public boolean retry(ITestResult iTestResult) {
        if (count < maxTry) {
            System.out.println("Retry test " + iTestResult.getName() + " with status " + this.getStatusName(iTestResult.getStatus()));
            count ++;
            return true;
        }
        count = 0;
        return false;
    }
    public String getStatusName(int status){
        String resultName = null;
        if (status == 1){
            resultName = "SUCCESS";
        }else if (status == 2){
            resultName = "FAILURE";
        }else if (status == 3) {
            resultName = "SKIP";
        }
        return resultName;
    }
}

//AnnotationRetryTransformer.java
package com.ehi.utils.Listeners;

import org.testng.IAnnotationTransformer;
import org.testng.annotations.ITestAnnotation;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class AnnotationRetryTransformer implements IAnnotationTransformer {
    @Override
    public void transform(ITestAnnotation annotation, Class testClass, Constructor testConstructor, Method testMethod) {
        annotation.setRetryAnalyzer(Retry.class);
    }
}
```

最后在 testng.xml 添加
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="N11 Test Suite" >
    <listeners>
        <listener class-name="com.ehi.utils.Listeners.AnnotationRetryTransformer"/>
        <listener class-name="com.ehi.Listeners.TestListener"/>

    </listeners>

    <test name="LoginTest">
        <classes>
            <class name="com.ehi.testcases.LoginTestCase"/>
        </classes>
    </test>
</suite>
```
这样我们就成功完成了两部分的功能，一个是失败时候的截图，一个case重跑。


# 集成到Jenkins上


# 结尾
这样我们就完成了一个简单的前端自动化测试框架，当然有很多的细节还没做好，比如说环境的切换，集成 docker，log 等等，但这是后面可以改善的内容，这篇文章的主要目的是学习 testng/allure 的配置和用法。

代码地址： https://github.com/01x01/Java-selenium-automation

