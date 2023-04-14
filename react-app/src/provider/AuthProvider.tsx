import { useEffect, useState } from "react";
import { AuthContext } from "../context/AuthContext";
import 'firebase/firestore';
import { auth } from "../firebaseSetup";
import * as React from 'react';
import 'firebase/auth';
import {User} from 'firebase/auth'


export const AuthProvider: React.FC = ({ children }) => {
  const [user, setUser] = useState<firebaseUser | null>(null);
  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged((firebaseUser) => {
      setUser(firebaseUser);
    });

    return unsubscribe;
  }, []);

  return <AuthContext.Provider value={user}>{children}</AuthContext.Provider>;
};