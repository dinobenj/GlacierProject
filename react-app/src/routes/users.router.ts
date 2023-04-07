import express, { Request, Response } from "express";
import { ObjectId } from "mongodb";
import { collections } from "../services/database.service";
import Game from "../user/users";

export const usersRouter = express.Router();

usersRouter.use(express.json());

