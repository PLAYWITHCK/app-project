package com.edusharehub;

public class Note {
    private final int id;
    private final String title;
    private final String subject;
    private final String price;
    private final boolean isFree;

    public Note(int id, String title, String subject, String price, boolean isFree) {
        this.id = id;
        this.title = title;
        this.subject = subject;
        this.price = price;
        this.isFree = isFree;
    }

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getSubject() {
        return subject;
    }

    public String getPrice() {
        return price;
    }

    public boolean isFree() {
        return isFree;
    }
}
