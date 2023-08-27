/*
  Warnings:

  - You are about to alter the column `cooldown` on the `Skill` table. The data in that column could be lost. The data in that column will be cast from `Double` to `VarChar(191)`.
  - You are about to alter the column `channeled` on the `Skill` table. The data in that column could be lost. The data in that column will be cast from `TinyInt` to `VarChar(191)`.

*/
-- AlterTable
ALTER TABLE `Skill` MODIFY `cooldown` VARCHAR(191) NULL DEFAULT '-',
    MODIFY `channeled` VARCHAR(191) NULL DEFAULT '';
