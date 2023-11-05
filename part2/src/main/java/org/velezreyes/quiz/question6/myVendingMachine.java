package org.velezreyes.quiz.question6;

public class myVendingMachine implements VendingMachine {
    private int insertedQuarters = 0;

    @Override
    public void insertQuarter() {
        insertedQuarters++;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        if (insertedQuarters < 3) {
            throw new NotEnoughMoneyException();
        }

        switch (name) {
            case "ScottCola":
                if (insertedQuarters >= 3) {
                    insertedQuarters -= 3;
                    return new ScottCola();
                } else {
                    throw new NotEnoughMoneyException();
                }
            case "KarenTea":
                if (insertedQuarters >= 4) {
                    insertedQuarters -= 4;
                    return new KarenTea();
                } else {
                    throw new NotEnoughMoneyException();
                }
            default:
                throw new UnknownDrinkException();
        }
    }
}
