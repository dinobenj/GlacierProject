import React from "react";
import 'firebase/auth';
import 'firebase/firestore';
import {User} from 'firebase/auth'

export const AuthContext = React.createContext<User | null>(null);