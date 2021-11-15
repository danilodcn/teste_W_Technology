import { useEffect, useState } from "react";
import { api } from "../services/api";

export const useLogin = () => {
  const [logging, setLogging] = useState([]);

  useEffect(() => {}, [logging]);

  function login() {
    const data = "grant_type=password&username=danilo&password=Danilo*1997";
    const auth =
      "Basic SWxVMGp3TVZjRzRlY0ZZTENYNlVublJqS0dqZG1hSmhEVlBPNWdEazpSU1NybWQzSFNlWE80YkpOMEJGUlAxSllBWGQyYU03aHRmcnU3aDhheTE4dER1RW9rUTI0dGtUNnFJc2ZSMnRrdHNaWENvOXU5RVB6d1ZjbTZ0VnFVazFZcUFPUlNrT3VnaFlJa3Vvbkpjdm1FN2IwWm15UWpaeGR0WkNDdlk0RA==";

    api.defaults.headers.common.Authorization = auth;
    api.post("o/token/", data);
  }

  return {
    logging,
    setLogging,
    login,
  };
};
