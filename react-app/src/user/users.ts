import { ObjectId } from "mongodb";

export default class User {
      constructor(public email: string, private password: string) {}
  }