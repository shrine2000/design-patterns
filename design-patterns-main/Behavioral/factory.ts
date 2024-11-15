// This class represents a button in iOS
class iOSButton {

}

// This class represents a button in Android
class AndroidButton {

}

/**
 * This class is a factory that creates buttons.
 * It has a method called `createButton` that takes an `os` argument and returns an `iOSButton` or an `AndroidButton` instance depending on the value of `os`.
 */
class ButtonFactory {
    /**
     * This method creates a new button instance based on the value of the `os` argument.
     * If `os` is "iOS", the method returns an `iOSButton` instance.
     * If `os` is anything else, the method returns an `AndroidButton` instance.
     * @param os - A string representing the operating system for which to create the button. Valid values are "iOS" and anything else.
     * @returns An instance of either `iOSButton` or `AndroidButton`.
     */
    createButton(os: string): iOSButton | AndroidButton {
        if (os === "iOS") {
            return new iOSButton();
        } else {
            return new AndroidButton();
        }
    }
}

// Create a new instance of the `ButtonFactory` class.
const factory = new ButtonFactory();

// Create a new button for iOS using the `createButton` method of the `ButtonFactory` class.
const buttonOne = factory.createButton("iOS");

// Create a new button for Android using the `createButton` method of the `ButtonFactory` class.
const buttonTwo = factory.createButton("Android");


//source - https://fireship.io/lessons/typescript-design-patterns/