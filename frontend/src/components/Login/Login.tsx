import * as React from "react";
import { Container, Input, Typography, Button } from "@mui/material";
import { palette, typography } from "../../theme";
import { useLogin } from "../../hooks/useLogin";

type LoginProps = {};

export const Login: React.FC<LoginProps> = (props) => {
  const { login } = useLogin();
  return (
    <Container>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
          gap: "10px",
        }}
      >
        <Typography
          color={palette.primary.main}
          style={{ paddingBottom: "1%", fontFamily: typography.fontFamily }}
        >
          Faça login para acessar o sistema
        </Typography>

        <Input
          placeholder="Entre com seu usuário"
          disableUnderline
          style={{ width: "20vw", borderColor: palette.secondary.main }}
          type="text"
          required
          sx={{ borderRadius: 2, border: 2, justifyContent: "center" }}
        />

        <Input
          placeholder="Senha"
          disableUnderline
          style={{ width: "20vw", borderColor: palette.secondary.main }}
          type="password"
          required
          sx={{ borderRadius: 2, border: 2, justifyContent: "center" }}
        />

        <Button
          style={{
            width: "20vw",
            borderColor: palette.secondary.main,
            backgroundColor: palette.secondary.main,
            color: palette.grey[400],
          }}
          onClick={() => login()}
        >
          Login
        </Button>
      </div>
    </Container>
  );
};
